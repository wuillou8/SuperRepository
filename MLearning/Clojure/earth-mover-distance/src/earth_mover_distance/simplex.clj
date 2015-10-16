(ns earth-mover-distance.simplex
  (:require [clojure.core.matrix :as m]
            [clojure.math.numeric-tower :as math]))
            ;[earth-mover-distance.emd :as emd]))
 
(def precis 0.00001)
  ; Heuristic explanation of the above code:
  ;
  ; The earth mover distance is solved by solving a transportation problem, given a supply, 
  ; a demand vectors as well as a cost function.
  ; The problem is formulated as a set of equations as shown below, that can be rephrased into a
  ; linear problem in normal form by the introduction of slack variables. As in the literature, 
  ; this can solved by the simplex method, whereas the problem values and conditions are put into
  ; a "tableau".
  ; 
  ; In the case of minimisation, the dual problem is optimised and the Von Neumann fundam. theorem
  ; ensures that the correct value was found. The resulting translation values f_ij are stored into
  ; the slack values after optimisation.
  ;
  ; The simplex maximisation:
  ; The idea is then to start the algo from a basic solution and through 
  ; operations done around the pivots, to move along the simplex vertices of largest increase
  ; up to the optimal solution.
  ; Proof: if the simplex hypersurface is convex, the algo has to converge, as far as I can see. amen.

(defn create-table
  ([emd-pbm]
   (create-table (:m-costs emd-pbm) (:v-supply emd-pbm) (:v-demand emd-pbm))) 
  ([cost-matrix supplyv demandv]
  ; cost-matrix is the ... cost-matrix::Matrix{float}
  ; supply and demand are Vector{float}
  ; The algorithm below transforms a transport optimisation problem into 
  ; table so that it can be optimised by the simplex algorithm.
  ;
  ; conditions for the earth mover problem:
  ;   C cost matrix,
  ;   f_ij earth transported from i(supply) to j(demand), notice that f_ij are the problem variables,
  ;   X_i supply from i,
  ;   Y_j demand from j,
  ;   Z quantity to optimize,
  ;   Z := \sum_i \sum_j C_ij f_ij,
  ;   f_ij >= 0,
  ;   \sum_i f_ij = Y_j (no more transport than demand),
  ;   \sum_j f_ij <= X_i (but no strict cond on the offer)
  ;
  ;   This is the way the table below is organised for the problem with supply size 3, demand size 2:
  ;
  ;   f_11 : f_12 : f_13 : f_21 : f_22 ...  val
  ;   -----------------------------------------
  ;   1    :  1   :  1   :  0   :  0   ...  X_1
  ;   0    :  0   :  0   :  1   :  1   ...  X_2 
  ;          ...
  ;
  ;   1    :  0   :  0   :  1   :  0   ...  Y_1
  ;   0    :  1   :  0   :  0   :  1   ...  Y_2
  ;          ...
  ;   -----------------------------------------
  ;   C_11 : C_12 : C_13 :  C_21       ...   0  
  ;   -----------------------------------------
  ;
  (let [[d-x d-y] (m/shape cost-matrix)
        n-slack 0 ; slack variables are zero if demand = supply, which is the case for now. otherwise, the condition \sum_i f_ij =< 
        n-y (+ d-y n-slack) ; + slack variables s_i's...

        ; 1) create an empty table of appropriate size
        [dim-x dim-y] [(+ 1 d-y d-x) (+ 1 n-slack (* d-x d-y))]
        table (m/zero-matrix dim-x dim-y)      
        ; 2) fill the table with the values representing the different conditions.
        ; storage as: [i-coord j-coord val]
        ; demand
        y-s (for [i (range d-x)] [i (- dim-y 1) (nth demandv i)])
        yy-s (for [i (range d-x) j (range d-y)]
               [i (+ i (* j d-y)) 1.]) 
        ; supply
        x-s (for [j (range d-y)] [(+ d-y j) (- dim-y 1) (nth supplyv j)])
        xx-s (for [i (range d-x) j (range d-y)]
               [(+ i d-y) (+ j (* i d-y)) 1.]) 
        ; correlations
        c-s (for [i (range d-x) j (range d-y)]
              [(+ d-x d-y) (+ j (* i d-y)) (m/mget cost-matrix i j)])
        ; values are stocked into an array of array so that the table can be filled appropiratedly: [[i-coord1 j-coord1 val1], [i-coord2 j-coord2 val2] ...]
        values-vect (concat x-s y-s c-s xx-s yy-s)
        ; values are set into the table 
        table (reduce (fn [t element]
                          (apply m/mset t element))
                          table
                          values-vect)]   
    table))) 

(defn table->dual [table]
  ; for an optimisation using the simplex approach, minimisation can be achieved
  ; transferring the table into its dual form, with additional slack variables.
  ; optimisation is done through standard simplex algorithm.
  ; The Von Neumann duality principle ensures that the maximised Z value of the dual problem is the minimal of the standard problem.
  (let [nb-slack (m/column-count table)
        nb-vars (m/row-count table)
        ; generate slack column elements
        slack-columns (for [i (range (- nb-slack 1))]
                  (-> (m/zero-vector nb-slack)
                      (m/mset i 1.)))
        
        ; transpose the matrix and add slack columnes
        table-T  (m/rows table)
        last-column (last table-T)

        ; construct dual table
        table* (m/transpose (apply m/join-along 0 (butlast table-T) slack-columns))
        table* (m/join-along 1 table* last-column)
        table* (m/multiply-row table* (- nb-slack 1) -1.)]       
    table*))

(defn check-optimality [s-tableau]
  (if (< 0 (count (filter #(< % 0) (last s-tableau))))
    false true))

(defn filter-pivot [ty tx]
    (if (> (math/abs tx) precis)
      (let [val (/ ty tx)
            val (if (>= val 0.) val Double/MAX_VALUE)]
        val)
      Double/MAX_VALUE))

(defn find-min-abs-key 
  ([array]
    ; for now...
    (first (apply min-key second (map-indexed vector (m/to-double-array array)))))
  ([array fn] 
    (first (apply min-key second (map-indexed vector (map #(fn %) (m/to-double-array array)))))))

(defn find-pivot [table]
  (let [enter-idx (find-min-abs-key (last table))
        x (butlast (m/slice table 1 enter-idx))
        y (butlast (last (m/columns table)))
        depart-idx (find-min-abs-key (map  filter-pivot y x))]
    [depart-idx enter-idx]))

(defn jordan-gauss-decompose-step [table pivot-i pivot-j]
    (let [nb-lines (first (m/shape table))
          pivot (float (m/mget table pivot-i pivot-j))
          pivot-row (m/slice table 0 pivot-i)]
        (loop [i 0 table table]
            (if (< i nb-lines)
                (let [t (if (not= i pivot-i)
                    (let [row (m/get-row table i)
                          fact (float (/ (m/mget row pivot-j) pivot))
                          row (m/sub row (m/mul pivot-row  fact))]
                      (m/set-row table i row))
              ; else pivot row
              (m/multiply-row table i (/ 1. pivot)))]
          (recur (inc i) t))
      table))))

(defn get-result-simplex [solved-table]
  (let [shape (m/shape solved-table)
        n-vars (- (second shape) (first shape))
        ; the minimum is on the latest row/column after optimisation
        minimum (m/mget solved-table (- (first shape) 1) (- (second shape) 1))
        ; the solution is in the latest row, where the dual problem slack variables are giving the values for the real problem x_i values. 
        solutionv (-> (m/rows solved-table) last
                      (subvec n-vars) butlast)
       ]
  {:minimum minimum :flow solutionv})) 

(defn simplex-method [table]
    (loop [t table] 
        (if (check-optimality t)
            t
            (recur (apply jordan-gauss-decompose-step t (find-pivot t))))))

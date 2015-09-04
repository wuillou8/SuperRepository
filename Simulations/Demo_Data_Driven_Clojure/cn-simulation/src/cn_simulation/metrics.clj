(ns cn-simulation.metrics
  (require [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]))

; general methods
(defn event->perfo [event perfo-fct] 
  (let [
        convs-list (:convs event)
        views-list (:views event)
        L-data     10000
        L-recomm   (-> views-list (count))
        ]
  (perfo-fct convs-list views-list L-data L-recomm)))

; INFORMATION RETRIEVAL metrics, as implemented in
; 8.3.2.2 Measuring Usage Prediction of:
; Recommender Systems Handbook, (Ricci, Rokach, Shapira, Kantor)
(def perf0-classical {:tp 0, :fp 0, :tn 0, :fn 0})

(defn add-perfo-classical 
  [p1 p2]
  { :tp ($= (:tp p1) + (:tp p2)), 
    :fp ($= (:fp p1) + (:fp p2)),
    :tn ($= (:tn p1) + (:tn p2)),
    :fn ($= (:fn p1) + (:fn p2))})

(defn perfo-classical 
  [convs-list views-list L-data L-recomm]
  (let [
        tp (count convs-list)
        ]
  (if (= 0 tp)
    { :tp tp, 
      :fp L-recomm, 
      :tn ($= L-data - L-recomm - 1), 
      :fn 1 }
    { :tp tp, 
      :fp ($= L-recomm - tp),
      :tn ($= L-data - L-recomm - tp),
      :fn tp })))

(defn make-perfo-classical
  [perf]
  (let [
        precis (if (= 0 ($= (:tp perf) + (:fp perf)))
                 1.
                 ($= float (:tp perf) / ((:tp perf) + (:fp perf))))        
        recall ($= float (:tp perf) / ((:tp perf) + (:fn perf)))
        specif ($= 1. - (:fp perf) / ((:fp perf) + (:tn perf)))
        f1 ($= 2. * precis * recall /(precis + recall))        
        ]
  {:precis precis, :recall recall, :specif specif, :f1 f1}))

(defn events->precision-perfo 
  ; function computing the info retrieval perfo
  [events]
  (let [
        data-perf-class (map #(event->perfo % perfo-classical) events)
        perf-classical (reduce add-perfo-classical perf0-classical data-perf-class)
        perf-tot-classical (make-perfo-classical perf-classical)
        ]
  perf-tot-classical))

; mean reciprocal rank: 
; for N experiments, 1/N * \sum_i 1/rank_i, 
; whereas rank_i is the rank of the item picked.  
(def perf0-mrr {:rr 0, :views 0})

(defn add-perfo-mrr 
  [p1 p2]
  { :rr ($= (:rr p1) + (:rr p2)),
    :views ($= (:views p1) + (:views p2))})

(defn perfo-mrr 
  [convs-list views-list L-data L-recomm]
  (let [ 
        m (sort (map #(.indexOf views-list %) convs-list) )
        ]
    (if (= 0 (count m))
      {:rr ($ 1. / (count views-list)) :views 1.}
      (let [
            rr   (sum (map #($= 1. / (% + 1) ) (first m)))
            L-rr (count m)
            ] 
        {:rr rr :views L-rr}))
  ))

(defn make-perfo-mrr 
  [perf]
  (let [
        mrr ($= float (:rr perf) / (:views perf))
        ]
  mrr))

(defn events->mrr-perfo
  ; function computing the mrr perfo
  [events]
  (let [
        data-perf-mrr (map #(event->perfo % perfo-mrr) events)
        perf-mrr (reduce add-perfo-mrr perf0-mrr  data-perf-mrr)
        perf-tot-mrr (make-perfo-mrr perf-mrr)
        ]
  {:mrr perf-tot-mrr, :views (:views perf-mrr)}))


; ~CTR: 
; conversion "per visit"  
(def perf0-ctr {:convs 0, :views 0})

(defn add-perfo-ctr 
  [p1 p2]
  { :convs ($= (:convs p1) + (:convs p2)),
    :views ($= (:views p1) + (:views p2))})

(defn perfo-ctr 
  [convs-list views-list L-data L-recomm]
  (let [ 
        convs (count convs-list)
        views (count views-list)
        ]
    {:convs convs :views views}))

(defn make-perfo-ctr 
  [perf]
  (let [
        ctr ($= float (:convs perf) / (:views perf))
        ]
  {:ctr ctr}))

(defn events->ctr-perfo
  ; function computing the mrr perfo
  [events]
  (let [
        data-perf-ctr (map #(event->perfo % perfo-ctr) events)
        perf-ctr (reduce add-perfo-ctr perf0-ctr  data-perf-ctr)
        perf-tot-ctr (make-perfo-ctr perf-ctr)
        ]
    perf-tot-ctr ))


//----------------------------------------------------------------
// A TEMPLATE FOR COMPUTING MLEARNING MODELS
//
//----------------------------------------------------------------

open System
open System.IO

//----------------------------------------------------------------
// Functional Read IN

let myInprocessFile1 (filePath : string) =
        seq{  // Sequences allow for lazy programming
            use fileReader = new StreamReader(filePath)

            //fileReader.ReadLine() |> ignore // ignore outputs () or unit

            while not fileReader.EndOfStream do
                let line = fileReader.ReadLine()
                let lIn = 
                    line.Split([| ' ' |], StringSplitOptions.RemoveEmptyEntries)
                    |> Seq.append  ["1"]  // Interceptor added
                yield Seq.toArray( Seq.map (fun x -> (float) x) lIn ) 
        }      

let myInprocessFile2 (filePath : string) =
        seq{  // Sequences allow for lazy programming
            use fileReader = new StreamReader(filePath)

            while not fileReader.EndOfStream do
                let line = fileReader.ReadLine()
                let lIn = line.Split([| ' ' |], StringSplitOptions.RemoveEmptyEntries)
                yield Seq.toArray ( Seq.map (fun x -> (float) x) lIn ) 
        }      

//-----------------------------------------------------------------------------
// Utilities

let sum i0 i1 f =
    let mutable t = 0.0
    for i in i0..i1 do
        t <- t + f i    
    t

let get_col (i : int) (arr : float [][]) =
         seq { for j in 0 .. ((Array.length arr)-1) do 
               yield  [| arr.[j].[i] |]
             }

let get_col2 (i : int) (arr : float [][]) =
         seq { for j in 0 .. ((Array.length arr)-1) do 
               yield  arr.[j].[i] 
             }

let get_avg (arr : float [][]) =
         let col = (Seq.toArray (get_col2 1 arr))
         Array.fold ( fun acc elem -> acc +  elem ) 0.0 col / (float) (Array.length col) 

let get_av (arr : float []) =
         Array.fold ( fun acc elem -> acc +  elem ) 0.0 (Seq.toArray arr) / (float) (Array.length arr) 

let get_normalised (arr : float [][]) (num : int) =
         let col = (Seq.toArray (get_col2 num arr))
         let avg = 
                Array.fold ( fun acc elem -> acc +  elem ) 0.0 col / (float) (Array.length col)
         let var = 
                (Array.fold ( fun acc elem -> acc + (elem - avg)**2.0 ) 0.0 (col)) 
         let var = (var / (float) (Array.length col))**0.5
         Array.map (fun x -> (x-avg)/var) col 

let multi (n : int) (x : float []) (y : float []) = 
         sum 0 (n-1) ( fun i -> x.[i] * y.[i] )

//-----------------------------------------------------------------------------
// Compute Quantities

let h_theta (theta : float [][]) (vect : float [][])  (numb : int)=
                   let n = (Array.length vect.[0]) //get_linesLength theta vect 
                   multi n theta.[0] vect.[numb] 
          
let new_theta (theta : float [][]) (arrX : float [][]) (arrY : float [][]) (alpha : float) = 
                   let N = Array.length arrX
                   let accr0 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[0] )       
                   let accr1 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[1] )  
                   let accr2 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[2] )  
                   [| [| theta.[0].[0] - alpha * accr0/(float)N ; theta.[0].[1] - alpha * accr1/(float)N; theta.[0].[2] - alpha * accr2/(float)N  |] |]

let J_theta (theta : float [][]) (arrX : float [][])  (arrY : float [][]) =
                   let N = Array.length arrX
                   1.0/((float) N) * ( sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] )**2.0 ) )

 
//------------------------------------------------------------------
//     				MAIN
//------------------------------------------------------------------

[<EntryPoint>]
let main (args : string []) =
    //printfn "Test: The Input is %A"  args

//----- Analysis (Lin Regression Spaghetti)
    let ex3xPath = "DATA/ex3x.dat"
    let ex3yPath = "DATA/ex3y.dat"
    let myX = myInprocessFile1 ex3xPath // readIn predictor and added an interceptor 
    let myY = myInprocessFile2 ex3yPath 
    let arrX = (Seq.toArray myX)
    let arrY = (Seq.toArray myY)
    
    // Normalisation & Test
    let arrX1 = get_normalised arrX 1
    let arrX2 = get_normalised arrX 2
    // Test
    printfn "chck0 %A %A" arrX1 arrX2
    printfn "check avg_1 %A" (Array.fold ( fun acc elem -> acc + elem ) 0.0 arrX1)   
    printfn "check x**2_1 %A" (Array.fold ( fun acc elem -> acc + (elem)**2.0 ) 0.0 arrX1) 
    printfn "check avg_2 %A" (Array.fold ( fun acc elem -> acc + elem ) 0.0 arrX1)   
    printfn "check x**2_2 %A" (Array.fold ( fun acc elem -> acc + (elem)**2.0 ) 0.0 arrX1) 
    
    // Run
    let ArrX = 
         Array.map2 (fun x y -> [| 1.0  ;x ; y |]) arrX1 arrX2
    printfn "arrayfinal: %A" ArrX
    let mutable thetaA = Array.init 1 (fun x -> [| 0.0; 0.0; 0.0 |])
    printfn "One Iteration: %A" ( new_theta  thetaA arrX arrY 1.0 )
    for i in 1 .. 1000 do
          thetaA <- ( new_theta  thetaA arrX arrY 0.07 )
          printfn "%d %f %f %f %f" i thetaA.[0].[0] thetaA.[0].[1] thetaA.[0].[2] ( J_theta thetaA arrX arrY )

//---- Final Output: main rturning a 0 or 1
    0

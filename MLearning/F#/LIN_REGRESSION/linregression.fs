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
                let myoutputType = "Array" // "Seq"    
                match myoutputType with   
                | "Array" -> yield Seq.toArray( Seq.map (fun x -> (float) x) lIn ) 
                // | "Seq" -> yield Seq.toArray( Seq.map (fun x -> (float) x) lIn )
                // | _  -> yield Seq.map (fun x -> (float) x) lIn
        }      

let myInprocessFile2 (filePath : string) =
        seq{  // Sequences allow for lazy programming
            use fileReader = new StreamReader(filePath)

            while not fileReader.EndOfStream do
                let line = fileReader.ReadLine()
                let lIn = line.Split([| ' ' |], StringSplitOptions.RemoveEmptyEntries)
                yield Seq.toArray ( Seq.map (fun x -> (float) x) lIn ) 
                // yield Seq.toArray ( Seq.map (fun x -> (float) x) lIn ) 
        }      

let sum i0 i1 f =
    let mutable t = 0.0
    for i in i0..i1 do
        t <- t + f i    
    t

let multi (n : int) (x : float []) (y : float []) = 
                   sum 0 (n-1) ( fun i -> x.[i] * y.[i] )

let h_theta (theta : float [][]) (vect : float [][])  (numb : int)=
                   let n = (Array.length vect.[0]) //get_linesLength theta vect 
                   multi n theta.[0] vect.[numb] 
          
let new_theta  (theta : float [][]) (arrX : float [][])  (arrY : float [][]) (alpha : float) = 
                   let N = Array.length arrX
                   let accr0 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[0] )       
                   let accr1 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[1] )  
                   [| theta.[0].[0] - alpha * accr0 ; theta.[0].[1] - alpha * accr1 |]


//------------------------------------------------------------------
//     				MAIN
//------------------------------------------------------------------

[<EntryPoint>]
let main (args : string []) =
    printfn "Test: The Input is %A"  args

//----- Analysis (Lin Regression Spaghetti)
    let ex2xPath = "DATA/ex2x.dat"
    let ex2yPath = "DATA/ex2y.dat"
    let myX = myInprocessFile1 ex2xPath // readIn predictor and added an interceptor 
    let myY = myInprocessFile2 ex2yPath 
    
    // Start Linear Regression
    let thetaA = Array.init (1) (fun x -> [| 0.0; 0.0 |])
    let arrX = (Seq.toArray myX)
    let arrY = (Seq.toArray myY)
    printfn "One Iteration: %A" ( new_theta  thetaA arrX arrY 0.07 )
//---- Final Output: main rturning a 0 or 1
    0

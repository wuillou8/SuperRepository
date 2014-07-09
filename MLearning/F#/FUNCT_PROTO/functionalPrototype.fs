//----------------------------------------------------------------
// A TEMPLATE FOR COMPUTING MLEARNING MODELS
//
//
//----------------------------------------------------------------

open System
open System.IO


// Analysis Class
type Analysis(modelType : string, predictFile : string, occuFile : string) =

    member A.modelType = modelType
    member A.predictFile = predictFile
    member A.occuFile = occuFile

type AnalysisFunct =
    | ModelType of string
    | PredictFile of string
    | OccuFile of string

type Model = 
    | LinearRegression
    | NaiveBayesian
    | MultiVarLinRegression
    | LogisticRegression 

// Functional Vector class
type Vector2D(x:double,y:double) =

    let norm2 = x*x + y*y

    member v.Dx = x
    member v.Dy = y

    member v.Length = sqrt(norm2)
    member v.Norm = norm2

let sum i0 i1 f =
    let mutable t = 0.0
    for i in i0..i1 do
        t <- t + f i    
    t

type Vector(xs: float []) =

    let xs = Array.copy xs

    member this.Dim = xs.Length

    member this.Item i = xs.[i]

    override this.ToString() =
        sprintf "%A" xs

    static member init n f =
        Vector(Array.init n f)

    static member (~-) (u: Vector) =
        Vector.init u.Dim (fun i -> -u.[i])

    static member (+) (u: Vector, v: Vector) =
        Vector.init u.Dim (fun i -> u.[i] + v.[i])

    static member (-) (u: Vector, v: Vector) =
        Vector.init u.Dim (fun i -> u.[i] - v.[i])

    static member (*) (u: Vector, v: Vector) =
        sum 0 (u.Dim-1) (fun i -> u.[i] * v.[i])


// Functional Read IN
//module myIO =
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
                | _  -> Seq.map (fun x -> (float) x) lIn
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



let get_vec xs = Vector( Array.ofSeq xs) 

exception Error1 of string


//let get_linesLength (theta : float [][]) (vect : float [][]) =
//                   if ( (Array.length theta.[0]) <> (Array.length vect.[0])) then
//                       raise(Error1("vbla error")) 
//                   else Array.length theta.[0]

//let get_filesLength (theta : float []) (vect : float [][]) =
//                   if ( (Array.length theta) <> (Array.length vect)) then
//                       raise(Error1("vbla error")) 
//                  else Array.length theta

let get_lengthtest  (theta : float []) (vect : float [][]) =
                   if ( (Array.length theta) <> (Array.length vect)) then
                       raise(Error1("vbla error")) 
                   else Array.length theta




let multi (n : int) (x : float []) (y : float []) =       // (numb : int) =
                   sum 0 (n-1) ( fun i -> x.[i] * y.[i] )

let h_theta (theta : float [][]) (vect : float [][])  (numb : int)=
                   let n = (Array.length vect.[0]) //get_linesLength theta vect 
                   multi n theta.[0] vect.[numb] 
          
let new_theta  (theta : float [][]) (arrX : float [][])  (arrY : float [][]) (alpha : float) = 
                   let N = Array.length arrX
                   let accr0 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[0] )       
                   let accr1 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[1] )  
                   [| theta.[0].[0] - alpha * accr0 ; theta.[0].[1] - alpha * accr1 |]


//-----------------------------------------accr1 = sum 0 (N-1) ( fun i -> ( (h_theta theta arrX i) - arrY.[i].[0] ) * arrX.[i].[0] )  -------------------------
//     MAIN PROGRAM
//------------------------------------------------------------------

[<EntryPoint>]
let main (args : string []) =
    printfn "Test: The meaning of life is %A"  args

// Analysis (Lin Regression Spaghetti)
    let ex2xPath = "DATA/ex2x.dat"
    let ex2yPath = "DATA/ex2y.dat"
    let myX = myInprocessFile1 ex2xPath // readIn predictor and added an interceptor 
    let myY = myInprocessFile2 ex2yPath 
    
    // Start Linear Regression
    let thetaA = Array.init (1) (fun x -> [| 0.0; 0.0 |])
    printfn "thetaAAA %A" thetaA

    //printfn "myX: %A" (Seq.nth 5 myX)
    printfn "myX: %A" (Seq.toArray myX)
    printfn "myY: %A" (Seq.toArray myY)
    let jair = seq {1 .. 55}
    printfn "%i %i" (Seq.length myX) (Seq.length myY)
 

    let fuck = Seq.toArray myX
    let gaton = fuck.[1].[0]
    printfn "gaton %A %A" fuck.[1] fuck.[1].[0]
    //printfn "last %A %A %A" gaton gaton.[0] (gaton.GetType()) //theta.[6]
    printfn "whoiscomp? %A %A" thetaA (thetaA.GetType())
    let arrX = Seq.toArray myX
    printfn " h_theta %A " ( h_theta thetaA (Seq.toArray myX) 2) // 2) 
    //printfn " %A " (get_lengthtest thetaA (Seq.toArray myX) 2)
    //let baston = (Seq.toArray myX)

//    printfn "test %A" (get_lengthtest thetaA.[1] baston.[1]) //
    let arrX = (Seq.toArray myX)
    let arrY = (Seq.toArray myY)
    printfn "voila: %A" ( new_theta  thetaA arrX arrY 0.07 )
//////// Final Output: main rturning a 0 or 1
    0

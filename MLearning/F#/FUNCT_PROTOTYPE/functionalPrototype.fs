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



// Functional Read IN
//module myIO =
let myInprocessFile (filePath : string) =
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
                | "Array" -> yield Seq.map (fun x -> (float) x) lIn 
                // | "Seq" 
                //     -> yield Seq.toArray( Seq.map (fun x -> (float) x) lIn )
                | _  -> Seq.map (fun x -> (float) x) lIn

        }      

let myfunc seq = 
            Seq.map  

//module main =

[<EntryPoint>]
let main (args : string []) =
    printfn "Test: The meaning of life is %A"  args


    let ex2Path = "DATA/ex4x.dat"
    let myIn = 
        myInprocessFile ex2Path 
    printfn "%A" myIn
    printfn "%A" (Seq.nth 5 myIn)
    printfn "%A" (Seq.toArray myIn)
    //
    0

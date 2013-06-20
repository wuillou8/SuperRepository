open System

open Vectors
open Matrices

//module Analysis =
//    open Vector

//[<EntryPoint>]
let main =
    printfn "Test: The meaning of life is %d" 23

    let vector xs = Vector(Array.ofSeq xs)
    vector [1.0..3.0]

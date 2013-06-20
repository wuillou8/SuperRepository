open System

open Vectors
open Matrices

//module Analysis =
//    open Vector

//[<EntryPoint>]
let main =
    printfn "Test: The meaning of life is %d" 23

    let vector ls = Vector(Array.ofSeq ls)
    vector [1.0..3.0] 
    // printf "myOutput %f" vector.Dim 
    // let v1 = vector [1.0..3.0] + vector [2.0..4.0]
    // 
    // let v2 = vector [1.0..3.0] * vector [2.0..4.0]
    let array1 = Array.create 10 "" 
    for i in 0 .. array1.Length - 1 do
        Array.set array1 i (i.ToString())
    for i in 0 .. array1.Length - 1 do
        printfn "%s " (Array.get array1 i)

    printfn "vector %A" (vector.ToString())
    printfn "bla %A" (vector [1.0..3.0])  

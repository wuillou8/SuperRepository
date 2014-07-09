

//namespace mainprogram
open System
open System.IO
open Vectors
open Matrices
open myIO
open Utils


//type MyClass(x: int) =
//   let mutable xx = x

//let myvar = new MyClass(12)
//module main =
[<EntryPoint>]
let main(args : string[]) = 
    printfn "Test: The meaning of life is %A" args

    let vector ls = Vector(Array.ofSeq ls)
    vector [1.0..3.0] 
    // printf "myOutput %f" vector.Dim 
    let v1 = vector [1.0..3.0] 
    let v2 = vector [2.0..4.0]
    let vv = v1 - v2
    printf  "v1%A v2%A v1-v2%A" v1 v2 vv
    // 
    let v2 = vector [1.0..3.0] * vector [2.0..4.0]
    printfn "%A" v2
    let array1 = Array.create 10 "" 
    for i in 0 .. array1.Length - 1 do
        Array.set array1 i (i.ToString())
    //for i in 0 .. array1.Length - 1 do
    //  printfn "%s " (Array.get array1 i)
    //
    //printfn "vector %A" (vector.ToString())
    //printfn "bla %A" (vector [1.0..3.0])  
    //let myarray = [| for i in 1 .. 7 -> i*i |]
    //let alphonse = Array.map (fun x -> 2*x) myarray
    //printfn "myarray and alphonse %A %A" myarray alphonse
    //printfn "stuff %A" myarray
    //printfn "fin %d" myarray.[5] ()
    //Input.rintreadlines "ex2y.dat"

    0 

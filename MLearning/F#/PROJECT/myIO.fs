// Contains IO methods

//[<RequireQualifieAccess>]
namespace myIO

open Vectors
open Matrices
open System
open System.IO
open System.Diagnostics

module Input = 

    let filex (Path : string) = File.ReadAllLines(Path) //"ex2Data/ex2x.dat");;
    let filey = File.ReadAllLines("ex2Data/ex2y.dat")

    let readLines (filePath : string) = System.IO.File.ReadLines(filePath)
    let readLines2 filePath = File.ReadAllLines(filePath) |> Seq.cast<string>
    let rintreadlines filePath = 
        let read = File.ReadAllLines(filePath)
        printfn "voici mon input %A" read


module Output =

    let funct a b =
        let myarray =  [|a..b|]
        Array.map (fun x -> 2*x) myarray
        printfn "myarrayinFunct %A" myarray
//        let vec = Vector(Array.ofSeq [1.0..5.0]) 

    let jair = //myIO.Output 1.0 x
        let x = 1
        printfn "voilou %d" x 
 

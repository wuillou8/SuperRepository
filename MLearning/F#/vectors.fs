// My Vectors class

// open Utils

namespace Vectors

open Utils
open Basics

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
        Basics.sum 0 (u.Dim-1) (fun i -> u.[i] * v.[i])


// MyMatrix class

namespace Matrices
open Vectors
open Utils

type Matrix(xs: float [,]) =
  let xs = Array2D.copy xs

  member __.Rows = xs.GetLength 0

  member __.Columns = xs.GetLength 1

  member this.Item(i, j) = xs.[i, j]

  override this.ToString() = sprintf "%A" xs

  static member init m n f = Matrix(Array2D.init m n f)

  static member (~-) (a: Matrix) =
    Matrix.init a.Rows a.Columns (fun i j -> -a.[i, j])

  static member (+) (a: Matrix, b: Matrix) =
    Matrix.init a.Rows a.Columns (fun i j -> a.[i, j] + b.[i, j])

  static member (-) (a: Matrix, b: Matrix) =
    Matrix.init a.Rows a.Columns (fun i j -> a.[i, j] - b.[i, j])

  static member (*) (a: Matrix, b: Matrix) =
    Matrix.init a.Rows b.Columns (fun i j ->
      Basics.sum 0 (b.Rows-1) (fun k -> a.[i, k] * b.[k, j]))


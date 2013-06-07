// my first fsharp script
open System.IO

open System
open System.Diagnostics

let gp =  
  new ProcessStartInfo
    (FileName = "gnuplot", UseShellExecute = false, 
     CreateNoWindow = true, RedirectStandardInput = true) 
  |> Process.Start


let filex = File.ReadAllLines("ex2Data/ex2x.dat");;
let filey = File.ReadAllLines("ex2Data/ex2y.dat");;



// Draw graph of two simple functions
gp.StandardInput.WriteLine "plot 'ex2Data/ex2x.dat' w l"  




printfn "Hello World"
let fileyy = File.ReadAllLines("ex2Data/ex2y.dat")


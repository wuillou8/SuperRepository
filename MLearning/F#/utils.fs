namespace Utils


module Basics =

    let sum i0 i1 f =
        let mutable t = 0.0
        for i in i0..i1 do
            t <- t + f i
        t

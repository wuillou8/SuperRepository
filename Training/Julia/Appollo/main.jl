# main.jl

using constants
using types
include("physics.jl")
include("moon.jl")
include("command-module.jl")
include("system.jl")


# Initialization of our bodies
earth = Body(ME, [0.0, 0.0], RE, ORIGIN)
moon = Moon(MM, [0., 0.], RM, moon_position(0.0))
command_module = Command_Module(MCM, INITIAL_VELOCITY, 5.0, INITIAL_POSITION)
world = System(0.0, earth, moon, command_module)

# Simulation's Run
function simulate()
    boost = 10. # m/s Change this to the correct value from the list above after everything else is done.
    position_list = Vector{Float64}[] # m
    current_time = 1.

    while current_time <= TOTAL_DURATION
        update(world, current_time, h)

        push(position_list, copy(world.command_module.position))

        current_time += 1
   end

    return position_list
end

@time pos = simulate()
writecsv("output.csv", pos)


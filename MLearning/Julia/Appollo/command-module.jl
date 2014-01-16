# command-module.jl

function acceleration(time::Float64, pos::Vector{Float64})
    moon_pos = moon_position(time) # Get the moon's position at this time

    distance_from_earth = pos # Earth is at the origin
    distance_to_moon = pos - moon_pos # Distance between command module and moon
    mag_e = magnitude(distance_from_earth) # Get the magnitude of this vector
    mag_m = magnitude(distance_to_moon)

    return -G * (ME * distance_from_earth / mag_e^3 + MM * distance_to_moon / mag_m^3)
end

function update(me::Command_Module, time::Float64)
    a = acceleration(time, me.position) # Calculate the acceleration on the module

    # Using Euler's method
    me.position += me.velocity # Increment position vector by velocity vector
    me.velocity += a # Add acceleration vector to velocity vector

    me
end

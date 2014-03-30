# system.jl

function update(me::System, time::Float64)
    # `me` is a reference to this instance of System

    me.time = time # Explicitly set the time on the system

    update(me.moon, time) # Update the moon
    update(me.command_module, time) # Update the command_module

    # TODO: Reach for the stars

    return me # Return the system
end

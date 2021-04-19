module Threaded

using ThreadedIterables: tmapreduce


function iterate_list(a_list::Vector{Vector{Float64}})
    count::Float64 = tmapreduce(x -> reduce(+, x), +, a_list)
    println(count)
    return count
end


end # module

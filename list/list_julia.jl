using PyCall

function iterate_list(a_list::Vector{Vector{Float64}})

    count = 0.0
    @inbounds for i in 1:length(a_list)
        internal_list = a_list[i]
        @simd for j in 1:length(internal_list)
            count += internal_list[j]
        end
    end
    println(count)
    return count
end


function make_list(a_list::Vector{Any})
    convert(Vector{Vector{Float64}}, a_list)
    @inbounds for i in 1:10^4
        new_list = zeros(10^4)
        @simd for j in 1:10^4
            new_list[j] = 0.01
        end
        push!(a_list, new_list)
    end
    return a_list
end

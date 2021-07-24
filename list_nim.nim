import nimpy  # https://github.com/yglukhov/nimpy

const length = 10_000  # 10^4  (10**4 in Python), DRY, specified in README doc.

proc iterate_list(a_list: openArray[seq[float]]): float {.exportpy.} =
  for i in 0 ..< a_list.len:
    for j in 0 ..< a_list[i].len:
      result += a_list[i][j]
  stdout.write result

func make_list(a_list: openArray[seq[float]]): seq[seq[float]] {.exportpy, noinit.} =
  result = newSeq[seq[float]](length)
  for i in 0 ..< length:
    var new_list = newSeqUninitialized[float](length)
    for j in 0 ..< length:
      new_list[j] = 0.01
    result[i] = new_list


# Notes: Can be made faster by replacing seq with array, because length is known.

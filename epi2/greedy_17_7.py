def get_max_bucket(heights):
    h1, h2, max_bucket = 0, len(heights) - 1, 0

    while h1 < h2:
        width = h2 - h1
        max_bucket = max(max_bucket, width * min(heights[h1], heights[h2]))
        if heights[h1] < heights[h2]:
            h1 += 1
        else:
            h2 -= 1

    return max_bucket
    
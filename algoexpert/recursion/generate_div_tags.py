# https://www.algoexpert.io/questions/generate-div-tags

# decision tree, 2 branches every iteration, except the case when opening == closing
def generateDivTags(numberOfTags):
    divs = ['<div>', '</div>']
    res, prefix = [], []

    def helper(opening, closing):
        if opening == closing == 0:
            res.append(''.join(prefix))
            return
        if opening > 0:
            prefix.append(divs[0])
            helper(opening - 1, closing)
            prefix.pop()
        if opening < closing:
            prefix.append(divs[1])
            helper(opening, closing - 1)
            prefix.pop()

    helper(numberOfTags, numberOfTags)
    return res


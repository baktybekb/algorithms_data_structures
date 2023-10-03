# https://www.algoexpert.io/questions/shorten-path

# O(n) time | O(n) space
def shortenPath(path):
    cleaned_path = filter(clean_path, path.split('/'))
    stack = []
    if path[0] == '/':
        stack.append('')
    for token in cleaned_path:
        if token == '..':
            if not stack or stack[-1] == '..':
                stack.append(token)
            elif stack[-1] != '':
                stack.pop()
        else:
            stack.append(token)
    if len(stack) == 1 and stack[0] == '':
        return '/'
    return '/'.join(stack)


def clean_path(token):
    return len(token) > 0 and token != '.'


if __name__ == '__main__':
    assert shortenPath('/foo/../test/../test/../foo//bar/./baz') == '/foo/bar/baz'
    assert shortenPath("/../../foo/bar/baz") == '/foo/bar/baz'


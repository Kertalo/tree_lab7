class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None


def find(root, key):
    if root is None:
        return None
    if key < root.key:
        return root.left
    elif key > root.key:
        return root.right
    else:
        return root


def add(root, key, parent=None):
    if root is None:
        return Node(key, parent)
    else:
        if key < root.key:
            root.left = add(root.left, key, root)
        else:
            root.right = add(root.right, key, root)
        return root


def delete(root, key):
    if root is None:
        return root
    else:
        if key < root.key:
            root.left = delete(root.left, key)
        elif key > root.key:
            root.right = delete(root.right, key)
        else:
            if root.right is None and root.left is None:
                return None
            elif root.right is None:
                root.left.parent = root
                return root.left
            elif root.left is None:
                root.right.parent = root
                return root.right
            else:
                root2 = root.right
                while root2.left is not None:
                    root2 = root2.left
                if root2.key != root.right.key:
                    root2.parent.left = root2.right
                    if root2.right is not None:
                        root2.right.parent = root2.parent
                root2.left = root.left
                root.left.parent = root2
                if root.right.key == root2.key:
                    root2.right = root.right.right
                else:
                    root2.right = root.right
                root2.right.parent = root2
                root2.parent = root.parent

                if root.parent.key > root.key:
                    root.parent.left = root
                else:
                    root.parent.right = root
                return root2
        return root


def build_bst(elements):
    root = None
    for element in elements:
        root = add(root, element)
    return root


def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.key, end=" ")
        print_inorder(root.right)


def print_tree(root, level=0):
    if root is not None:
        #print(root.key)
        print_tree(root.right, level+1)
        print("    "*level + str(root.key))
        print_tree(root.left, level+1)


def klava():
    # Ввод данных с клавиатуры
    elements = []
    n = int(input("Введите количество элементов: "))
    print("Введите элементы:")
    for i in range(n):
        element = int(input("Элемент #{}: ".format(i+1)))
        elements.append(element)

    # Построение двоичного дерева поиска
    root = build_bst(elements)

    # Вывод элементов в порядке возрастания
    print("Элементы в порядке возрастания:")
    print_inorder(root)

    # Вывод дерева
    print("Дерево:")
    print_tree(root)
    return root


def read_elements_from_file(filename):
    try:
        with open(filename) as f:
            elements = [int(num) for num in f.read().split()]
        return elements
    except (FileNotFoundError, PermissionError):
        print("Ошибка при чтении файла")
        return []


def build_bst_from_elements(elements):
    root = None
    for element in elements:
        root = add(root, element)
    return root


def build_bst_from_file(filename):
    elements = read_elements_from_file(filename)
    if elements:
        return build_bst(elements)
    else:
        return None


def file(filename):
    # Ввод данных с файла
    root = build_bst_from_file(filename)

    # Вывод элементов в порядке возрастания
    print("Элементы в порядке возрастания:")
    print_inorder(root)
    print("")
    # Вывод дерева
    print("Дерево:")
    print_tree(root)
    return root


# Пример использования
# root = klava()
root = file('tree.txt')
add(root, 9)
add(root, 8)
add(root, 11)
print_tree(root)
delete(root, 7)
print("")
print("")
print_tree(root)

root2 = find(root, 8)
print("")
print(root2.left.key)
print(root2.right.key)
print(root2.key)
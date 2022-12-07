"""Day 7: No Space Left On Device"""

import os.path

from typing import List, Dict, Optional
from util import assert2, text_input, file_input

example_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class Node(object):
    def __init__(
        self,
        name: str,
        size: int = 0,
        parent: Optional["Node"] = None,
    ):
        self.name = name
        self.size = size
        self.children: List[Node] = []
        self.parent = parent

    def add(self, node: "Node") -> "Node":
        node.parent = self
        self.children.append(node)
        return node

    def parents(self) -> List["Node"]:
        parents: List[Node] = []
        node = self
        while node.parent is not None:
            if len(node.children) > 0:
                parents.append(node)
            node = node.parent
        parents.append(node)
        parents.reverse()
        return parents


def dir_sizes(node: Node, sizes: Dict[str, int]) -> Dict[str, int]:
    for child in node.children:
        if len(child.children) > 0:
            dir_sizes(child, sizes)
        else:
            parent_names = [node.name for node in child.parents()]
            for i in range(len(parent_names)):
                path = os.path.join(*parent_names[0 : i + 1])
                sizes[path] = sizes.get(path, 0) + child.size
    return sizes


def parse_cmds(cmds: List[str]) -> Node:
    root = Node("/")
    node = root
    listing = False
    for cmd in cmds:
        if listing:
            size, _, name = cmd.partition(" ")
            if size.isdigit():
                node.add(Node(name, int(size)))
        if cmd.startswith("$ cd"):
            listing = False
            cwd = cmd[5:]
            if cwd == "/":
                node = root
            elif cwd == "..":
                if node.parent is None:
                    raise ValueError("root dir has no parent")
                node = node.parent
            else:
                node = node.add(Node(cwd))
        elif cmd.startswith("$ ls"):
            listing = True
    return root


def day7_1(lines: List[str]) -> int:
    sizes = dir_sizes(parse_cmds(lines), {})
    return sum(size for _, size in sizes.items() if size <= 100_000)


assert2(95437, day7_1(text_input(example_input, str)))
assert2(1206825, day7_1(file_input(7, str)))


def day7_2(lines: List[str]) -> int:
    sizes = dir_sizes(parse_cmds(lines), {})
    min_to_free = 30_000_000 - (70_000_000 - sizes["/"])
    return min(size for _, size in sizes.items() if size >= min_to_free)


assert2(24933642, day7_2(text_input(example_input, str)))
assert2(9608311, day7_2(file_input(7, str)))

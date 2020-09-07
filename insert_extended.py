class Element:
    """
    helps you insert elements at multiple indices by using the index from the original list
    similar to list.insert(position,element) but both positions and elements could be more than one
    therefore a list of positions and a list of elements in the positions

    syntax:
    Element.insert_multiple_elements(old_list, pos_list, elements_list)
    """

    def __init__(self):
        pass

    @classmethod
    def sort_elements(cls, pos, elements):
        x = [[pos[i], elements[i]] for i in range(len(pos))]
        sorted_pos = sorted(x)
        return sorted_pos

    @classmethod
    def change_positions(cls, pos, elements):
        sorted_list = Element.sort_elements(pos, elements)
        new_pos = [sorted_list[0][0]]
        for i in range(len(sorted_list)):
            if i > 0:
                x = sorted_list[i][0] + i
                new_pos.append(x)
        return new_pos

    @staticmethod
    def insert_multiple_elements(list, pos_list, elements_list):
        x = Element.change_positions(pos_list, elements_list)
        # print(x)
        sorted_positions = Element.sort_elements(pos_list, elements_list)
        # print(sorted_positions)
        for i in range(len(elements_list)):
            list.insert(x[i], sorted_positions[i][1])
        return list

# # elements to be inserted
# elements = ['(', ')', '-', " "]
# # original_positions
# pos = [0, 3, 6, 6]
# # list where you need the elements inserted
# old_list = [8, 9, 9, 1, 5, 4, 3, 6, 2, 1]
# # # # Desired output: ['(', 8, 9, 9, ')', 1, 5, 4, '-', ' ', 3, 6, 2, 1]
#
# print(Element.insert_multiple_elements(old_list, pos, elements))




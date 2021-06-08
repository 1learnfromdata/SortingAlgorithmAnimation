from manim import *


class SortCodeAlgo(GraphScene,Scene):

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label=r"Time(seconds)",
            # x_axis_label="Iteration",
            y_max = 50,
            y_min = 0,
            x_max= 10000,
            x_min= 0,
            # y_tick_frequency= 3,
            # x_tick_frequency= 3,
            y_axis_config =  {"tick_frequency": 10},
            x_axis_config = {"tick_frequency": 1000},
            axes_color= BLUE,
            **kwargs
        )


    def construct(self):

        def create_rectange(x, y, z, color_fill):
            EXPLAIN_WIDTH = x
            EXPLAIN_HEIGHT = y
            explain_filled_rect = Rectangle(
                width=EXPLAIN_WIDTH,
                height=EXPLAIN_HEIGHT,
                stroke_width=1,
                fill_color=color_fill
            )
            explain_filled_rect.shift(z)
            explain_filled_rect.set_fill(color_fill, 0.5)
            self.play(GrowFromCenter(explain_filled_rect, run_time=1))
            explain_line_left, explain_line_bottom = [
                Line(
                    explain_filled_rect.get_corner(start),
                    explain_filled_rect.get_corner(end),
                    color=RED_A
                )
                for start, end in [(DL, UL), (DL, DR)]
            ]

            self.play(
                GrowFromEdge(explain_line_left, DOWN),
                GrowFromEdge(explain_line_bottom, LEFT)
            )

        def currentTextPositionMarkup(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text))
            return index_text

        def currentTextPositionText(name, size_of_text, color_text, position):
            index_text = Text(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text))
            return index_text

        def currentTextPositionMarkupWithout(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            return index_text


        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Bubble Sort</b></span>',
                      1.2, GREEN_B, 3.5 * UP + 0.6 * LEFT)

        fixed_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Python Code</b></span>',
                      0.4, TEAL_D, 3 * UP + 6 * LEFT)

        create_rectange(7.1, 6.8, 0.54 * DOWN + 3.5 * LEFT, DARK_GRAY)

        left_fixed_text1 = currentTextPositionMarkup(r'<span font_family="monospace"><b>Time Complexity</b></span>',
                      0.5, PURPLE_A, 2.7 * UP + 1.7 * RIGHT)

        left_fixed_text2 = currentTextPositionMarkup(r'<span font_family="monospace"><b>Best Case : </b></span>',
                      0.35, YELLOW_C, 2.3 * UP + 1 * RIGHT)

        left_fixed_text3 = currentTextPositionMarkup(r'<span font_family="monospace"><b>Average Case : </b></span>',
                      0.35, YELLOW_C, 1.9 * UP + 1.2 * RIGHT)

        left_fixed_text4 = currentTextPositionMarkup(r'<span font_family="monospace"><b>Worst Case : </b></span>',
                      0.35, YELLOW_C, 1.5 * UP + 1.1 * RIGHT)

        left_fixed_text6 = currentTextPositionMarkup(r'<span font_family="monospace"><b>Space Complexity : </b></span>',
                      0.5, MAROON_C, 1 * UP + 2 * RIGHT)



        

        # ----     buble sort code ----------

        sort_full_code1 = """def bubble_sort(arr):\n   n = len(arr)\n   for i in range(n-1):\n      for j in range(0, n-i-1):\n         if arr[j] > arr[j+1] :\n            arr[j], arr[j+1] = arr[j+1], arr[j]"""


        # self.play(Write(MarkupText(f'<span font_family="monospace"><b>{sort_full_code}</b></span>',color=WHITE).scale(0.5)))

        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{sort_full_code1}</b></span>',
                      0.37, GREY_A, 1.7 * UP + 3.55 * LEFT)

        code_text1[0:3].set_color(ORANGE)  # DEF
        code_text1[3:14].set_color(YELLOW_C)  # bubble_sort
        code_text1[22:25].set_color(BLUE_C)   # len
        code_text1[30:33].set_color(GREEN_E)   # for
        code_text1[34:36].set_color(GREEN_E)   # in
        code_text1[36:41].set_color(BLUE_C)    # range
        code_text1[47:50].set_color(GREEN_E)
        code_text1[51:53].set_color(GREEN_E)
        code_text1[53:58].set_color(GREEN_E)
        code_text1[68:70].set_color(GREEN_E)
        self.play(Write(code_text1))

        sort_full_code2 = """if __name__ == "__main__":\n   arr = [41,9,3,25,28,39,19,47,4,50,21,8]\n   bubble_sort(arr)\n   print("Sorted array is:")\n   print(arr)"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{sort_full_code2}</b></span>',
                      0.37, GREY_A, 0.4 * DOWN + 3.9 * LEFT)
        code_text2[0:2].set_color(GREEN_E)
        code_text2[12:22].set_color(GREEN_E)
        code_text2[76:81].set_color(BLUE_C)
        code_text2[82:98].set_color(GREEN_C)   # string
        code_text2[99:104].set_color(BLUE_C)
        self.play(Write(code_text2))


        sort_full_code3 = """Code Output\n\nSorted array is:\n[3, 4, 8, 9, 19, 21, 25, 28, 39, 41, 47, 50]"""

        code_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{sort_full_code3}</b></span>',
                      0.37, WHITE, 2.4 * DOWN + 3.7 * LEFT)
        code_text3[0:10].set_color(MAROON_B)
        self.play(Write(code_text3))

        left_fixed_text7 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text7.next_to(left_fixed_text2)
        self.play(Write(left_fixed_text7))

        left_fixed_text8 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text8.next_to(left_fixed_text3)
        self.play(Write(left_fixed_text8))

        left_fixed_text9 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text9.next_to(left_fixed_text4)
        self.play(Write(left_fixed_text9))


        left_fixed_text10 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(1)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text10.next_to(left_fixed_text6)
        self.play(Write(left_fixed_text10))

        # graph-----------

        self.y_axis_label=r"Time(Milliseconds)"
        self.y_max = 80000
        self.y_min = 0
        self.x_max= 11000
        self.x_min= 0
        self.y_axis_config =  {"tick_frequency": 20000}
        self.x_axis_config = {"tick_frequency": 1000}
        self.axes_color= BLUE


        data = [9.7,  156.35,  722.89,  20183,   76263]
        x = [100,     500,   1000,  5000,   10000]
        self.setup_axes()

        init_label_y = 0
        end_label_y = 80000
        step_y = 20000
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        init_label_x = 0
        end_label_x = 11000
        step_x = 2000
        self.x_axis.label_direction = DOWN
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))

        
        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())
        l4 = Line(dot_collection[3].get_center(), dot_collection[4].get_center())
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis,l1,l2,l3,l4)
        group2.scale(0.6)
        group2.shift(2 * DOWN + 3 * RIGHT)
        group2.remove(l4)
        group2.remove(l3)
        group2.remove(l2)
        group2.remove(l1)

        self.play(ShowIncreasingSubsets(group2))
        iteration_label = currentTextPositionMarkupWithout('<span font_family="monospace"><b>Array Length</b></span>',
                      0.4, GREY_A, 3.74 * DOWN + 3 * RIGHT)
        self.play(Write(iteration_label))

        graph_inner_label = currentTextPositionMarkup('<span font_family="monospace"><b>Array Length:\n    Time(ms):</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 2.1 * RIGHT)

        graph_number1 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>500\n156.35</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number1))
        self.play(FadeIn(l1))
        graph_number2 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>1000\n722.89</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number2),FadeOut(graph_number1))
        self.play(FadeIn(l2))
        graph_number3 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>5000\n20183</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number3),FadeOut(graph_number2))
        self.play(FadeIn(l3))
        graph_number4 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>10000\n76263</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number4),FadeOut(graph_number3))
        self.play(FadeIn(l4))



        # -------------- selection sort starts -----------------------

        self.play(FadeOut(left_fixed_text7), FadeOut(left_fixed_text8),FadeOut(left_fixed_text9),FadeOut(left_fixed_text10),
                  FadeOut(code_text1), FadeOut(code_text2),FadeOut(code_text3), FadeOut(group2),FadeOut(l1),
                  FadeOut(l2),FadeOut(l3),FadeOut(l4), FadeOut(top_disapper_text),
                  FadeOut(graph_number4),
                  FadeOut(graph_inner_label), FadeOut(iteration_label))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Selection Sort</b></span>',
                      1.2, BLUE_D, 3.5 * UP + 0.6 * LEFT)

        selection_full_code1 = """def selection_sort(arr):\n   for i in range(len(arr)):\n      min_idx = i\n      for j in range(i + 1, len(arr)):\n         if arr[min_idx] > arr[j]:\n            min_idx = j\n      arr[i],arr[min_idx]=arr[min_idx],arr[i]"""


        # self.play(Write(MarkupText(f'<span font_family="monospace"><b>{sort_full_code}</b></span>',color=WHITE).scale(0.5)))

        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{selection_full_code1}</b></span>',
                      0.37, GREY_A, 1.7 * UP + 3.63 * LEFT)

        code_text1[0:3].set_color(ORANGE)  # DEF
        code_text1[3:17].set_color(YELLOW_C)  # bubble_sort
        code_text1[23:26].set_color(GREEN_E)   # for
        code_text1[27:29].set_color(GREEN_E)   # in
        code_text1[29:34].set_color(BLUE_C)   # range
        code_text1[35:38].set_color(BLUE_C)    # len
        code_text1[54:57].set_color(GREEN_E)
        code_text1[58:60].set_color(GREEN_E)
        code_text1[60:65].set_color(BLUE_C)
        code_text1[70:73].set_color(BLUE_C)
        code_text1[80:82].set_color(GREEN_E)
        self.play(Write(code_text1))

        selection_full_code2 = """if __name__ == "__main__":\n   arr = [41,9,3,25,28,39,19,47,4,50,21,8]\n   selection_sort(arr)\n   print("Sorted array is:")\n   print(arr)"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{selection_full_code2}</b></span>',
                      0.37, GREY_A, 0.4 * DOWN + 3.9 * LEFT)
        code_text2[0:2].set_color(GREEN_E)
        code_text2[12:22].set_color(GREEN_E)
        code_text2[79:84].set_color(BLUE_C)
        code_text2[85:101].set_color(GREEN_C)   # string
        code_text2[102:107].set_color(BLUE_C)
        self.play(Write(code_text2))


        output_full_code3 = """Code Output\n\nSorted array is:\n[3, 4, 8, 9, 19, 21, 25, 28, 39, 41, 47, 50]"""

        code_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{output_full_code3}</b></span>',
                      0.37, WHITE, 2.4 * DOWN + 3.7 * LEFT)
        code_text3[0:10].set_color(MAROON_B)
        self.play(Write(code_text3))

        left_fixed_text7 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text7.next_to(left_fixed_text2)
        self.play(Write(left_fixed_text7))

        left_fixed_text8 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text8.next_to(left_fixed_text3)
        self.play(Write(left_fixed_text8))

        left_fixed_text9 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text9.next_to(left_fixed_text4)
        self.play(Write(left_fixed_text9))


        left_fixed_text10 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text10.next_to(left_fixed_text6)
        self.play(Write(left_fixed_text10))

        # graph-----------

        self.y_axis_label=r"Time(Milliseconds)"
        self.y_max = 50000
        self.y_min = 0
        self.x_max= 11000
        self.x_min= 0
        self.y_axis_config =  {"tick_frequency": 10000}
        self.x_axis_config = {"tick_frequency": 1000}
        self.axes_color= BLUE


        data = [9.7,  87.94,  361.51,  10573,   48039]
        x = [100,     500,   1000,  5000,   10000]
        self.setup_axes()

        init_label_y = 0
        end_label_y = 50000
        step_y = 10000
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        init_label_x = 0
        end_label_x = 11000
        step_x = 2000
        self.x_axis.label_direction = DOWN
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))

        
        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())
        l4 = Line(dot_collection[3].get_center(), dot_collection[4].get_center())
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis,l1,l2,l3,l4)
        group2.scale(0.6)
        group2.shift(2 * DOWN + 3 * RIGHT)
        group2.remove(l4)
        group2.remove(l3)
        group2.remove(l2)
        group2.remove(l1)

        self.play(ShowIncreasingSubsets(group2))
        iteration_label = currentTextPositionMarkupWithout('<span font_family="monospace"><b>Array Length</b></span>',
                      0.4, GREY_A, 3.74 * DOWN + 3 * RIGHT)
        self.play(Write(iteration_label))

        graph_inner_label = currentTextPositionMarkup('<span font_family="monospace"><b>Array Length:\n    Time(ms):</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 2.1 * RIGHT)

        graph_number1 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>500\n87.94</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number1))
        self.play(FadeIn(l1))
        graph_number2 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>1000\n361.51</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number2),FadeOut(graph_number1))
        self.play(FadeIn(l2))
        graph_number3 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>5000\n10573</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number3),FadeOut(graph_number2))
        self.play(FadeIn(l3))
        graph_number4 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>10000\n48039</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number4),FadeOut(graph_number3))
        self.play(FadeIn(l4))

        # ----     insertion sort code ----------

        self.play(FadeOut(left_fixed_text7), FadeOut(left_fixed_text8),FadeOut(left_fixed_text9),FadeOut(left_fixed_text10),
                  FadeOut(code_text1), FadeOut(code_text2),FadeOut(code_text3), FadeOut(group2),FadeOut(l1),
                  FadeOut(l2),FadeOut(l3),FadeOut(l4), FadeOut(top_disapper_text),
                  FadeOut(graph_number4),
                  FadeOut(graph_inner_label), FadeOut(iteration_label))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Insertion Sort</b></span>',
                      1.2, GREEN_SCREEN, 3.5 * UP + 0.6 * LEFT)


        insertion_full_code1 = """def insertion_sort(arr):\n   for i in range(1, len(arr)):\n      key = arr[i]\n      j = i-1\n      while j >= 0 and key  arr[j]:\n         arr[j + 1] = arr[j]\n         j -= 1\n         arr[j + 1] = key"""


        # self.play(Write(MarkupText(f'<span font_family="monospace"><b>{sort_full_code}</b></span>',color=WHITE).scale(0.5)))

        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{insertion_full_code1}</b></span>',
                      0.37, GREY_A, 1.7 * UP + 4.4 * LEFT)

        code_text1[0:3].set_color(ORANGE)  # DEF
        code_text1[3:17].set_color(YELLOW_C)  # bubble_sort
        code_text1[23:26].set_color(GREEN_E)   # for
        code_text1[27:29].set_color(GREEN_E)   # in
        code_text1[29:34].set_color(BLUE_C)   # range
        code_text1[37:40].set_color(BLUE_C)    # len
        code_text1[62:67].set_color(GREEN_E)
        code_text1[71:74].set_color(GREEN_E)
        less_than = Text('<',color=GREY_A,opacity=1).scale(0.37)
        less_than.shift(1.55 * UP + 3 * LEFT)
        self.play(Write(code_text1))
        self.add(less_than)

        insertion_full_code2 = """if __name__ == "__main__":\n   arr = [41,9,3,25,28,39,19,47,4,50,21,8]\n   insertion_sort(arr)\n   print("Sorted array is:")\n   print(arr)"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{insertion_full_code2}</b></span>',
                      0.37, GREY_A, 0.4 * DOWN + 3.9 * LEFT)
        code_text2[0:2].set_color(GREEN_E)
        code_text2[12:22].set_color(GREEN_E)
        code_text2[79:84].set_color(BLUE_C)
        code_text2[85:101].set_color(GREEN_E)   # string
        code_text2[102:107].set_color(BLUE_C)
        self.play(Write(code_text2))


        output_full_code3 = """Code Output\n\nSorted array is:\n[3, 4, 8, 9, 19, 21, 25, 28, 39, 41, 47, 50]"""

        code_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{output_full_code3}</b></span>',
                      0.37, WHITE, 2.4 * DOWN + 3.7 * LEFT)
        code_text3[0:10].set_color(MAROON_B)
        self.play(Write(code_text3))

        left_fixed_text7 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text7.next_to(left_fixed_text2)
        self.play(Write(left_fixed_text7))

        left_fixed_text8 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text8.next_to(left_fixed_text3)
        self.play(Write(left_fixed_text8))

        left_fixed_text9 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text9.next_to(left_fixed_text4)
        self.play(Write(left_fixed_text9))


        left_fixed_text10 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(1)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text10.next_to(left_fixed_text6)
        self.play(Write(left_fixed_text10))

        # graph-----------


        self.y_axis_label=r"Time(Milliseconds)"
        self.y_max = 50000
        self.y_min = 0
        self.x_max= 11000
        self.x_min= 0
        self.y_axis_config =  {"tick_frequency": 10000}
        self.x_axis_config = {"tick_frequency": 1000}
        self.axes_color= BLUE


        data = [9.7,  68.40,  429.17,  12449,   48853]
        x = [100,     500,   1000,  5000,   10000]
        self.setup_axes()

        init_label_y = 0
        end_label_y = 50000
        step_y = 10000
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        init_label_x = 0
        end_label_x = 11000
        step_x = 2000
        self.x_axis.label_direction = DOWN
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))

        
        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())
        l4 = Line(dot_collection[3].get_center(), dot_collection[4].get_center())
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis,l1,l2,l3,l4)
        group2.scale(0.6)
        group2.shift(2 * DOWN + 3 * RIGHT)
        group2.remove(l4)
        group2.remove(l3)
        group2.remove(l2)
        group2.remove(l1)

        self.play(ShowIncreasingSubsets(group2))
        iteration_label = currentTextPositionMarkupWithout('<span font_family="monospace"><b>Array Length</b></span>',
                      0.4, GREY_A, 3.74 * DOWN + 3 * RIGHT)
        self.play(Write(iteration_label))

        graph_inner_label = currentTextPositionMarkup('<span font_family="monospace"><b>Array Length:\n    Time(ms):</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 2.1 * RIGHT)

        graph_number1 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>500\n68.40</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number1))
        self.play(FadeIn(l1))
        graph_number2 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>1000\n429.17</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number2),FadeOut(graph_number1))
        self.play(FadeIn(l2))
        graph_number3 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>5000\n12449</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number3),FadeOut(graph_number2))
        self.play(FadeIn(l3))
        graph_number4 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>10000\n48853</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number4),FadeOut(graph_number3))
        self.play(FadeIn(l4))


        # ----     Merge sort code ----------

        self.play(FadeOut(left_fixed_text7), FadeOut(left_fixed_text8),FadeOut(left_fixed_text9),FadeOut(left_fixed_text10),
                  FadeOut(code_text1), FadeOut(code_text2),FadeOut(code_text3), FadeOut(group2),FadeOut(l1),
                  FadeOut(l2),FadeOut(l3),FadeOut(l4), FadeOut(top_disapper_text), FadeOut(less_than),
                  FadeOut(graph_number4),
                  FadeOut(graph_inner_label), FadeOut(iteration_label))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Merge Sort</b></span>',
                      1.2, PURPLE_A, 3.5 * UP + 0.6 * LEFT)

        merge_full_code1 = """def merge_sort(arr):\n   if len(arr) > 1:\n      mid = len(arr) // 2\n      L = arr[:mid]\n      R = arr[mid:]\n      merge_sort(L)\n      merge_sort(R)\n      i = j = k = 0\n      while i   len(L) and j   len(R):\n         if L[i]   R[j]:\n            arr[k] = L[i]\n            i += 1\n         else:\n            arr[k] = R[j]\n            j += 1\n         k += 1\n      while i  len(L):\n         arr[k] = L[i]\n         i += 1\n         k += 1\n      while j  len(R):\n         arr[k] = R[j]\n         j += 1\n         k += 1"""


        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{merge_full_code1}</b></span>',
                      0.27, GREY_A, 0.3 * UP + 4.9 * LEFT)

        code_text1[0:3].set_color(ORANGE)  # DEF
        code_text1[3:13].set_color(YELLOW_C)  # bubble_sort
        code_text1[19:21].set_color(GREEN_E)   # for
        code_text1[21:24].set_color(BLUE_C)   # in
        code_text1[36:39].set_color(BLUE_C)   # range
        code_text1[102:107].set_color(GREEN_E)    # len
        code_text1[108:111].set_color(BLUE_C)
        code_text1[118:121].set_color(BLUE_C)
        code_text1[125:127].set_color(GREEN_E)
        code_text1[151:155].set_color(GREEN_E)
        code_text1[175:180].set_color(GREEN_E)
        code_text1[181:184].set_color(BLUE_C)
        code_text1[207:212].set_color(GREEN_E)
        code_text1[213:216].set_color(BLUE_C)

        less_than1 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than1.shift(1.03 * UP + 5.3 * LEFT)
        self.play(Write(code_text1))
        self.add(less_than1)

        less_than2 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than2.shift(1.03 * UP + 3.75 * LEFT)
        self.add(less_than2)

        less_than3 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than3.shift(0.8 * UP + 5 * LEFT)
        self.add(less_than3)

        less_than4 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than4.shift(0.65 * DOWN + 5.4 * LEFT)
        self.add(less_than4)

        less_than5 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than5.shift(1.5 * DOWN + 5.4 * LEFT)
        self.add(less_than5)

        merge_full_code2 = """if __name__ == "__main__":\n   arr = [41,9,3,25,28,39,19,47,4,50,21,8]\n   merge_sort(arr)\n   print(f"Sorted array is: {arr}")"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{merge_full_code2}</b></span>',
                      0.27, GREY_A, 2.7 * DOWN + 4.7 * LEFT)
        code_text2[0:2].set_color(GREEN_E)
        code_text2[12:22].set_color(GREEN_E)
        code_text2[75:80].set_color(BLUE_C)
        code_text2[81:98].set_color(GREEN_E)   # string
        code_text2[101:103].set_color(GREEN_E)
        self.play(Write(code_text2))


        output_full_code3 = """Code Output\n\nSorted array is: [3, 4, 8, 9, 19, 21, 25, 28, 39, 41, 47, 50]"""

        code_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{output_full_code3}</b></span>',
                      0.27, WHITE, 3.55 * DOWN + 3.7 * LEFT)
        code_text3[0:10].set_color(MAROON_B)
        self.play(Write(code_text3))

        left_fixed_text7 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n log(n))  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text7.next_to(left_fixed_text2)
        self.play(Write(left_fixed_text7))

        left_fixed_text8 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n log(n))  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text8.next_to(left_fixed_text3)
        self.play(Write(left_fixed_text8))

        left_fixed_text9 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n log(n))  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text9.next_to(left_fixed_text4)
        self.play(Write(left_fixed_text9))


        left_fixed_text10 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text10.next_to(left_fixed_text6)
        self.play(Write(left_fixed_text10))

        # graph-----------

        self.y_axis_label=r"Time(Milliseconds)"
        self.y_max = 300
        self.y_min = 0
        self.x_max= 11000
        self.x_min= 0
        self.y_axis_config =  {"tick_frequency": 50}
        self.x_axis_config = {"tick_frequency": 1000}
        self.axes_color= BLUE


        data = [9.7,  9.9,  19.54,  117.26,   263.83]
        x = [100,     500,   1000,  5000,   10000]
        self.setup_axes()

        init_label_y = 0
        end_label_y = 300
        step_y = 50
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        init_label_x = 0
        end_label_x = 11000
        step_x = 2000
        self.x_axis.label_direction = DOWN
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))

        
        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())
        l4 = Line(dot_collection[3].get_center(), dot_collection[4].get_center())
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis,l1,l2,l3,l4)
        group2.scale(0.6)
        group2.shift(2 * DOWN + 3 * RIGHT)
        group2.remove(l4)
        group2.remove(l3)
        group2.remove(l2)
        group2.remove(l1)

        self.play(ShowIncreasingSubsets(group2))
        iteration_label = currentTextPositionMarkupWithout('<span font_family="monospace"><b>Array Length</b></span>',
                      0.4, GREY_A, 3.74 * DOWN + 3 * RIGHT)
        self.play(Write(iteration_label))

        graph_inner_label = currentTextPositionMarkup('<span font_family="monospace"><b>Array Length:\n    Time(ms):</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 2.1 * RIGHT)

        graph_number1 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>500\n9.9</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number1))
        self.play(FadeIn(l1))
        graph_number2 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>1000\n19.54</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number2),FadeOut(graph_number1))
        self.play(FadeIn(l2))
        graph_number3 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>5000\n117.26</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number3),FadeOut(graph_number2))
        self.play(FadeIn(l3))
        graph_number4 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>10000\n263.83</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number4),FadeOut(graph_number3))
        self.play(FadeIn(l4))


        # ----     Quick sort code ----------


        self.play(FadeOut(left_fixed_text7), FadeOut(left_fixed_text8),FadeOut(left_fixed_text9),FadeOut(left_fixed_text10),
                  FadeOut(code_text1), FadeOut(code_text2),FadeOut(code_text3), FadeOut(group2),FadeOut(l1),
                  FadeOut(l2),FadeOut(l3),FadeOut(l4), FadeOut(top_disapper_text), FadeOut(less_than1),
                  FadeOut(less_than5),FadeOut(less_than4),FadeOut(less_than3),FadeOut(less_than2),
                  FadeOut(graph_number4),
                  FadeOut(graph_inner_label), FadeOut(iteration_label))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Quick Sort</b></span>',
                      1.2, GREEN_A, 3.5 * UP + 0.6 * LEFT)


        quick_full_code1 = """def partition(start, end, array):\n   pivot_index = start\n   pivot = array[pivot_index]\n   while start   end:\n      while start   len(array) and array[start]  = pivot:\n         start += 1\n      while array[end] > pivot:\n         end -= 1\n      if start   end:\n         array[start], array[end] = array[end], array[start]\n   array[end],array[pivot_index] = array[pivot_index],array[end]\n   return end\n\ndef quick_sort(start, end, array):\n   if start   end:\n      p = partition(start, end, array)\n      quick_sort(start, p - 1, array)\n      quick_sort(p + 1, end, array)"""


        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{quick_full_code1}</b></span>',
                      0.27, GREY_A, 0.85 * UP + 3.48 * LEFT)

        code_text1[0:3].set_color(ORANGE)  # DEF
        code_text1[3:12].set_color(YELLOW_C)  # bubble_sort
        code_text1[71:76].set_color(GREEN_E)   # while
        code_text1[85:90].set_color(GREEN_E)   # while
        code_text1[95:98].set_color(BLUE_C)   # len
        code_text1[105:108].set_color(GREEN_E)    # and
        code_text1[135:140].set_color(GREEN_E)
        code_text1[163:165].set_color(GREEN_E)
        code_text1[280:286].set_color(GREEN_E)
        code_text1[289:292].set_color(GREEN_E)
        code_text1[292:302].set_color(YELLOW_C)
        code_text1[320:322].set_color(GREEN_E)

        less_than1 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than1.shift(2 * UP + 5.2 * LEFT)
        self.play(Write(code_text1))
        self.add(less_than1)

        less_than2 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than2.shift(1.8 * UP + 4.9 * LEFT)
        self.add(less_than2)

        less_than3 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than3.shift(1.8 * UP + 1.73 * LEFT)
        self.add(less_than3)

        less_than4 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than4.shift(0.95 * UP + 5.25 * LEFT)
        self.add(less_than4)

        less_than5 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        less_than5.shift(0.3 * DOWN + 5.58 * LEFT)
        self.add(less_than5)

        quick_full_code2 = """if __name__ == "__main__":\n   arr = [41,9,3,25,28,39,19,47,4,50,21,8]\n   quick_sort(0, len(arr) - 1, arr)\n   print(f"Sorted array is: {arr}")"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{quick_full_code2}</b></span>',
                      0.27, GREY_A, 1.7 * DOWN + 4.7 * LEFT)
        code_text2[0:2].set_color(GREEN_E)
        code_text2[12:22].set_color(GREEN_E)
        code_text2[73:76].set_color(BLUE_C)
        code_text2[88:93].set_color(BLUE_C)   # string
        code_text2[94:111].set_color(GREEN_E)
        code_text2[114:116].set_color(GREEN_E)
        self.play(Write(code_text2))


        output_full_code3 = """Code Output\n\nSorted array is: [3, 4, 8, 9, 19, 21, 25, 28, 39, 41, 47, 50]"""

        code_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{output_full_code3}</b></span>',
                      0.27, WHITE, 2.7 * DOWN + 3.7 * LEFT)
        code_text3[0:10].set_color(MAROON_B)
        self.play(Write(code_text3))

        left_fixed_text7 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n log(n))  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text7.next_to(left_fixed_text2)
        self.play(Write(left_fixed_text7))

        left_fixed_text8 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n log(n))  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text8.next_to(left_fixed_text3)
        self.play(Write(left_fixed_text8))

        left_fixed_text9 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n^2)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text9.next_to(left_fixed_text4)
        self.play(Write(left_fixed_text9))


        left_fixed_text10 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text10.next_to(left_fixed_text6)
        self.play(Write(left_fixed_text10))

        # graph-----------

        self.y_axis_label=r"Time(Milliseconds)"
        self.y_max = 300
        self.y_min = 0
        self.x_max= 11000
        self.x_min= 0
        self.y_axis_config =  {"tick_frequency": 50}
        self.x_axis_config = {"tick_frequency": 1000}
        self.axes_color= BLUE


        data = [9.7,  9.8,  18.65,  97.7,   224.7]
        x = [100,     500,   1000,  5000,   10000]
        self.setup_axes()

        init_label_y = 0
        end_label_y = 300
        step_y = 50
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        init_label_x = 0
        end_label_x = 11000
        step_x = 2000
        self.x_axis.label_direction = DOWN
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))

        
        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())
        l4 = Line(dot_collection[3].get_center(), dot_collection[4].get_center())
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis,l1,l2,l3,l4)
        group2.scale(0.6)
        group2.shift(2 * DOWN + 3 * RIGHT)
        group2.remove(l4)
        group2.remove(l3)
        group2.remove(l2)
        group2.remove(l1)

        self.play(ShowIncreasingSubsets(group2))
        iteration_label = currentTextPositionMarkupWithout('<span font_family="monospace"><b>Array Length</b></span>',
                      0.4, GREY_A, 3.74 * DOWN + 3 * RIGHT)
        self.play(Write(iteration_label))

        graph_inner_label = currentTextPositionMarkup('<span font_family="monospace"><b>Array Length:\n    Time(ms):</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 2.1 * RIGHT)

        graph_number1 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>500\n9.8</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number1))
        self.play(FadeIn(l1))
        graph_number2 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>1000\n18.65</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number2),FadeOut(graph_number1))
        self.play(FadeIn(l2))
        graph_number3 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>5000\n97.7</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number3),FadeOut(graph_number2))
        self.play(FadeIn(l3))
        graph_number4 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>10000\n224.7</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number4),FadeOut(graph_number3))
        self.play(FadeIn(l4))


        # ----     Timsort code ----------

        self.play(FadeOut(left_fixed_text7), FadeOut(left_fixed_text8),FadeOut(left_fixed_text9),FadeOut(left_fixed_text10),
                  FadeOut(code_text1), FadeOut(code_text2),FadeOut(code_text3), FadeOut(group2),FadeOut(l1),
                  FadeOut(l2),FadeOut(l3),FadeOut(l4), FadeOut(top_disapper_text), FadeOut(less_than1),
                  FadeOut(less_than5),FadeOut(less_than4),FadeOut(less_than3),FadeOut(less_than2),
                  FadeOut(graph_number4),
                  FadeOut(graph_inner_label), FadeOut(iteration_label))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>TimSort</b></span>',
                      1.2, TEAL_A, 3.5 * UP + 0.6 * LEFT)

        tim_full_code1 = """MIN_MERGE = 32
def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n # 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] # arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1"""


        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{tim_full_code1}</b></span>',
                      0.2, GREY_A, 1.7 * UP + 4.9 * LEFT)

        tim2_full_code1 = """def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i # len1 and j # len2:
        if left[i] #= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i # len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j # len2:
        arr[k] = right[j]
        k += 1
        j += 1"""


        code1_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{tim2_full_code1}</b></span>',
                      0.2, GREY_A, 1.4 * DOWN + 5.5 * LEFT)

        tim3_full_code1 = """def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(arr, start, end)
    size = minRun
    while size # n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right=min((left+2*size-1),(n-1))
            if mid # right:
                merge(arr, left, mid, right)
        size = 2 * size"""


        code2_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{tim3_full_code1}</b></span>',
                      0.2, GREY_A, 0.8 * DOWN + 2 * LEFT)

        # less_than1 = Text('<',color=GREY_A,opacity=1).scale(0.27)
        # less_than1.shift(2 * UP + 5.2 * LEFT)
        self.play(Write(code_text1),
            Write(code1_text1),
            Write(code2_text1)
            )

        quick_full_code2 = """if __name__ == "__main__":\n   arr = [41,9,3,25,28,39,19,47,4,50,21,8]\n   timSort(arr)\n   print("Sorted array is:")\n   print(arr)"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{quick_full_code2}</b></span>',
                      0.2, GREY_A, 2.4 * DOWN + 2 * LEFT)
        self.play(Write(code_text2))


        output_full_code3 = """Code Output\n\nSorted array is: \n[3,4,8,9,19,21,25,28,39,41,47,50]"""

        code_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{output_full_code3}</b></span>',
                      0.2, WHITE, 3.3 * DOWN + 2.7 * LEFT)
        self.play(Write(code_text3))

        left_fixed_text7 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text7.next_to(left_fixed_text2)
        self.play(Write(left_fixed_text7))

        left_fixed_text8 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n log(n))  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text8.next_to(left_fixed_text3)
        self.play(Write(left_fixed_text8))

        left_fixed_text9 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n log(n))  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text9.next_to(left_fixed_text4)
        self.play(Write(left_fixed_text9))


        left_fixed_text10 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>   O(n)  </b></span>',
                      0.5, WHITE, 2.7 * UP + 1.7 * RIGHT)
        left_fixed_text10.next_to(left_fixed_text6)
        self.play(Write(left_fixed_text10))

        # graph-----------

        # self.tim_sort_init()
        self.y_axis_label=r"Time(Milliseconds)"
        self.y_max = 300
        self.y_min = 0
        self.x_max= 11000
        self.x_min= 0
        self.y_axis_config =  {"tick_frequency": 50}
        self.x_axis_config = {"tick_frequency": 1000}
        self.axes_color= BLUE


        data = [9.7,    9.8,   19.54,     127,   283]
        x = [100,        500,   1000,    5000,   10000]
        self.setup_axes()

        init_label_y = 0
        end_label_y = 300
        step_y = 50
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        init_label_x = 0
        end_label_x = 11000
        step_x = 2000
        self.x_axis.label_direction = DOWN
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))

        
        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())
        l4 = Line(dot_collection[3].get_center(), dot_collection[4].get_center())
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis,l1,l2,l3,l4)
        group2.scale(0.6)
        group2.shift(2 * DOWN + 3 * RIGHT)
        group2.remove(l4)
        group2.remove(l3)
        group2.remove(l2)
        group2.remove(l1)

        self.play(ShowIncreasingSubsets(group2))
        iteration_label = currentTextPositionMarkupWithout('<span font_family="monospace"><b>Array Length</b></span>',
                      0.4, GREY_A, 3.74 * DOWN + 3 * RIGHT)
        self.play(Write(iteration_label))

        graph_inner_label = currentTextPositionMarkup('<span font_family="monospace"><b>Array Length:\n    Time(ms):</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 2.1 * RIGHT)

        graph_number1 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>500\n9.8</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number1))
        self.play(FadeIn(l1))
        graph_number2 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>1000\n19.54</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number2),FadeOut(graph_number1))
        self.play(FadeIn(l2))
        graph_number3 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>5000\n127</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number3),FadeOut(graph_number2))
        self.play(FadeIn(l3))
        graph_number4 = currentTextPositionMarkupWithout('<span font_family="monospace"><b>10000\n283</b></span>',
                      0.3, GREY_A, 0.4 * DOWN + 3.3 * RIGHT)
        self.play(Write(graph_number4),FadeOut(graph_number3))
        self.play(FadeIn(l4))

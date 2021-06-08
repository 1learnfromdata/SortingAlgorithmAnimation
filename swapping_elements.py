from manim import *


class SortFunction(Scene):
    def construct(self):

        def square_text_box(number, square_color, text_color):
            square = Square(side_length=0.7)
            square.set_stroke(color=square_color)
            text = MarkupText(number, color=text_color)
            text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text

        def square_swap(color_name):
            square_fill2 = Square(side_length=0.7)
            square_fill2.set_stroke(color=color_name, width=0)
            square_fill2.set_fill(color=color_name, opacity=0.5)

            return square_fill2


        bubs_text41 = square_text_box('41', BLUE_D, GREEN_B)
        bubs_text41.shift(3 * UP, 6 * LEFT)

        bubs_text9 = square_text_box('9', BLUE_D, GREEN_B)
        bubs_text9.next_to(bubs_text41, buff=0)

        bubs_text3 = square_text_box('3', BLUE_D, GREEN_B)
        bubs_text3.next_to(bubs_text9, buff=0)

        bubs_text25 = square_text_box('25', BLUE_D, GREEN_B)
        bubs_text25.next_to(bubs_text3, buff=0)

        bubs_text28 = square_text_box('28', BLUE_D, GREEN_B)
        bubs_text28.next_to(bubs_text25, buff=0)

        bubs_text39 = square_text_box('39', BLUE_D, GREEN_B)
        bubs_text39.next_to(bubs_text28, buff=0)

        bubs_text19 = square_text_box('19', BLUE_D, GREEN_B)
        bubs_text19.next_to(bubs_text39, buff=0)

        bubs_text47 = square_text_box('47', BLUE_D, GREEN_B)
        bubs_text47.next_to(bubs_text19, buff=0)

        bubs_text4 = square_text_box('4', BLUE_D, GREEN_B)
        bubs_text4.next_to(bubs_text47, buff=0)

        bubs_text50 = square_text_box('50', BLUE_D, GREEN_B)
        bubs_text50.next_to(bubs_text4, buff=0)

        bubs_text21 = square_text_box('21', BLUE_D, GREEN_B)
        bubs_text21.next_to(bubs_text50, buff=0)

        bubs_text8 = square_text_box('8', BLUE_D, GREEN_B)
        bubs_text8.next_to(bubs_text21, buff=0)

        bubs_text_right = MarkupText(r'<span font_family="monospace"><b>Bubble Sort</b></span>', 
                                    color=GREEN_B)

        bubs_text_right.shift(3 * UP + 5 * RIGHT)

        self.play(GrowFromCenter(bubs_text41), GrowFromCenter(bubs_text9), GrowFromCenter(bubs_text3),
                  GrowFromCenter(bubs_text25),
                  GrowFromCenter(bubs_text47), GrowFromCenter(bubs_text19), GrowFromCenter(bubs_text39),
                  GrowFromCenter(bubs_text28),
                  GrowFromCenter(bubs_text4), GrowFromCenter(bubs_text50), GrowFromCenter(bubs_text21),
                  GrowFromCenter(bubs_text8), Write(bubs_text_right))


        # ---------------- selection sort ----------------------

        sels_text41 = square_text_box('41', GOLD_C, BLUE_D)
        sels_text41.shift(1.8 * UP, 6 * LEFT)

        sels_text9 = square_text_box('9', GOLD_C, BLUE_D)
        sels_text9.next_to(sels_text41, buff=0)

        sels_text3 = square_text_box('3', GOLD_C, BLUE_D)
        sels_text3.next_to(sels_text9, buff=0)

        sels_text25 = square_text_box('25', GOLD_C, BLUE_D)
        sels_text25.next_to(sels_text3, buff=0)

        sels_text28 = square_text_box('28', GOLD_C, BLUE_D)
        sels_text28.next_to(sels_text25, buff=0)

        sels_text39 = square_text_box('39', GOLD_C, BLUE_D)
        sels_text39.next_to(sels_text28, buff=0)

        sels_text19 = square_text_box('19', GOLD_C, BLUE_D)
        sels_text19.next_to(sels_text39, buff=0)

        sels_text47 = square_text_box('47', GOLD_C, BLUE_D)
        sels_text47.next_to(sels_text19, buff=0)

        sels_text4 = square_text_box('4', GOLD_C, BLUE_D)
        sels_text4.next_to(sels_text47, buff=0)

        sels_text50 = square_text_box('50', GOLD_C, BLUE_D)
        sels_text50.next_to(sels_text4, buff=0)

        sels_text21 = square_text_box('21', GOLD_C, BLUE_D)
        sels_text21.next_to(sels_text50, buff=0)

        sels_text8 = square_text_box('8', GOLD_C, BLUE_D)
        sels_text8.next_to(sels_text21, buff=0)

        sels_text_right = MarkupText(r'<span font_family="monospace"><b>Selection Sort</b></span>', 
                                    color=BLUE_D).scale(0.85)

        sels_text_right.shift(1.8 * UP + 4.8 * RIGHT)

        self.play(GrowFromCenter(sels_text41), GrowFromCenter(sels_text9), GrowFromCenter(sels_text3),
                  GrowFromCenter(sels_text25),
                  GrowFromCenter(sels_text47), GrowFromCenter(sels_text19), GrowFromCenter(sels_text39),
                  GrowFromCenter(sels_text28),
                  GrowFromCenter(sels_text4), GrowFromCenter(sels_text50), GrowFromCenter(sels_text21),
                  GrowFromCenter(sels_text8), Write(sels_text_right))


        # ------------ insertion sort ---------------------------

        inss_text41 = square_text_box('41', TEAL_D, GREEN_SCREEN)
        inss_text41.shift(0.6 * UP, 6 * LEFT)

        inss_text9 = square_text_box('9', TEAL_D, GREEN_SCREEN)
        inss_text9.next_to(inss_text41, buff=0)

        inss_text3 = square_text_box('3', TEAL_D, GREEN_SCREEN)
        inss_text3.next_to(inss_text9, buff=0)

        inss_text25 = square_text_box('25', TEAL_D, GREEN_SCREEN)
        inss_text25.next_to(inss_text3, buff=0)

        inss_text28 = square_text_box('28', TEAL_D, GREEN_SCREEN)
        inss_text28.next_to(inss_text25, buff=0)

        inss_text39 = square_text_box('39', TEAL_D, GREEN_SCREEN)
        inss_text39.next_to(inss_text28, buff=0)

        inss_text19 = square_text_box('19', TEAL_D, GREEN_SCREEN)
        inss_text19.next_to(inss_text39, buff=0)

        inss_text47 = square_text_box('47', TEAL_D, GREEN_SCREEN)
        inss_text47.next_to(inss_text19, buff=0)

        inss_text4 = square_text_box('4', TEAL_D, GREEN_SCREEN)
        inss_text4.next_to(inss_text47, buff=0)

        inss_text50 = square_text_box('50', TEAL_D, GREEN_SCREEN)
        inss_text50.next_to(inss_text4, buff=0)

        inss_text21 = square_text_box('21', TEAL_D, GREEN_SCREEN)
        inss_text21.next_to(inss_text50, buff=0)

        inss_text8 = square_text_box('8', TEAL_D, GREEN_SCREEN)
        inss_text8.next_to(inss_text21, buff=0)

        inss_text_right = MarkupText(r'<span font_family="monospace"><b>Insertion Sort</b></span>', 
                                    color=GREEN_SCREEN).scale(0.85)

        inss_text_right.shift(0.6 * UP + 4.8 * RIGHT)

        self.play(GrowFromCenter(inss_text41), GrowFromCenter(inss_text9), GrowFromCenter(inss_text3),GrowFromCenter(inss_text25),
                  GrowFromCenter(inss_text47),GrowFromCenter(inss_text19), GrowFromCenter(inss_text39), GrowFromCenter(inss_text28),
                  GrowFromCenter(inss_text4), GrowFromCenter(inss_text50), GrowFromCenter(inss_text21),GrowFromCenter(inss_text8),
                  Write(inss_text_right))


        # ------------------- Merge Sort ----------------------

        mers_text41 = square_text_box('41', YELLOW_C, PURPLE_A)
        mers_text41.shift(0.8 * DOWN, 6 * LEFT)

        mers_text9 = square_text_box('9', YELLOW_C, PURPLE_A)
        mers_text9.next_to(mers_text41, buff=0)

        mers_text3 = square_text_box('3', YELLOW_C, PURPLE_A)
        mers_text3.next_to(mers_text9, buff=0)

        mers_text25 = square_text_box('25', YELLOW_C, PURPLE_A)
        mers_text25.next_to(mers_text3, buff=0)

        mers_text28 = square_text_box('28', YELLOW_C, PURPLE_A)
        mers_text28.next_to(mers_text25, buff=0)

        mers_text39 = square_text_box('39', YELLOW_C, PURPLE_A)
        mers_text39.next_to(mers_text28, buff=0)

        mers_text19 = square_text_box('19', YELLOW_C, PURPLE_A)
        mers_text19.next_to(mers_text39, buff=0)

        mers_text47 = square_text_box('47', YELLOW_C, PURPLE_A)
        mers_text47.next_to(mers_text19, buff=0)

        mers_text4 = square_text_box('4', YELLOW_C, PURPLE_A)
        mers_text4.next_to(mers_text47, buff=0)

        mers_text50 = square_text_box('50', YELLOW_C, PURPLE_A)
        mers_text50.next_to(mers_text4, buff=0)

        mers_text21 = square_text_box('21', YELLOW_C, PURPLE_A)
        mers_text21.next_to(mers_text50, buff=0)

        mers_text8 = square_text_box('8', YELLOW_C, PURPLE_A)
        mers_text8.next_to(mers_text21, buff=0)


        merss_text_right = MarkupText(r'<span font_family="monospace"><b>Merge Sort</b></span>', 
                                    color=PURPLE_A)

        merss_text_right.shift(0.8 * DOWN + 4.5 * RIGHT)

        self.play(GrowFromCenter(mers_text41), GrowFromCenter(mers_text9), GrowFromCenter(mers_text3),GrowFromCenter(mers_text25),
                  GrowFromCenter(mers_text47),GrowFromCenter(mers_text19), GrowFromCenter(mers_text39), GrowFromCenter(mers_text28),
                  GrowFromCenter(mers_text4), GrowFromCenter(mers_text50), GrowFromCenter(mers_text21),GrowFromCenter(mers_text8),
                  Write(merss_text_right))

        # ------------------ Quick sort ----------------


        quis_text41 = square_text_box('41', MAROON_C, GREEN_A)
        quis_text41.shift(2 * DOWN, 6 * LEFT)

        quis_text9 = square_text_box('9', MAROON_C, GREEN_A)
        quis_text9.next_to(quis_text41, buff=0)

        quis_text3 = square_text_box('3', MAROON_C, GREEN_A)
        quis_text3.next_to(quis_text9, buff=0)

        quis_text25 = square_text_box('25', MAROON_C, GREEN_A)
        quis_text25.next_to(quis_text3, buff=0)

        quis_text28 = square_text_box('28', MAROON_C, GREEN_A)
        quis_text28.next_to(quis_text25, buff=0)

        quis_text39 = square_text_box('39', MAROON_C, GREEN_A)
        quis_text39.next_to(quis_text28, buff=0)

        quis_text19 = square_text_box('19', MAROON_C, GREEN_A)
        quis_text19.next_to(quis_text39, buff=0)

        quis_text47 = square_text_box('47', MAROON_C, GREEN_A)
        quis_text47.next_to(quis_text19, buff=0)

        quis_text4 = square_text_box('4', MAROON_C, GREEN_A)
        quis_text4.next_to(quis_text47, buff=0)

        quis_text50 = square_text_box('50', MAROON_C, GREEN_A)
        quis_text50.next_to(quis_text4, buff=0)

        quis_text21 = square_text_box('21', MAROON_C, GREEN_A)
        quis_text21.next_to(quis_text50, buff=0)

        quis_text8 = square_text_box('8', MAROON_C, GREEN_A)
        quis_text8.next_to(quis_text21, buff=0)


        quis_text_right = MarkupText(r'<span font_family="monospace"><b>Quick Sort</b></span>', 
                                    color=GREEN_A)

        quis_text_right.shift(2 * DOWN + 4.5 * RIGHT)

        self.play(GrowFromCenter(quis_text41), GrowFromCenter(quis_text9), GrowFromCenter(quis_text3),GrowFromCenter(quis_text25),
                  GrowFromCenter(quis_text47),GrowFromCenter(quis_text19), GrowFromCenter(quis_text39), GrowFromCenter(quis_text28),
                  GrowFromCenter(quis_text4), GrowFromCenter(quis_text50), GrowFromCenter(quis_text21),GrowFromCenter(quis_text8),

                  Write(quis_text_right))


        # ---------------- timsort------------------


        tims_text41 = square_text_box('41', PURPLE_A, TEAL_A)
        tims_text41.shift(3.2 * DOWN, 6 * LEFT)

        tims_text9 = square_text_box('9', PURPLE_A, TEAL_A)
        tims_text9.next_to(tims_text41, buff=0)

        tims_text3 = square_text_box('3', PURPLE_A, TEAL_A)
        tims_text3.next_to(tims_text9, buff=0)

        tims_text25 = square_text_box('25', PURPLE_A, TEAL_A)
        tims_text25.next_to(tims_text3, buff=0)

        tims_text28 = square_text_box('28', PURPLE_A, TEAL_A)
        tims_text28.next_to(tims_text25, buff=0)

        tims_text39 = square_text_box('39', PURPLE_A, TEAL_A)
        tims_text39.next_to(tims_text28, buff=0)

        tims_text19 = square_text_box('19', PURPLE_A, TEAL_A)
        tims_text19.next_to(tims_text39, buff=0)

        tims_text47 = square_text_box('47', PURPLE_A, TEAL_A)
        tims_text47.next_to(tims_text19, buff=0)

        tims_text4 = square_text_box('4', PURPLE_A, TEAL_A)
        tims_text4.next_to(tims_text47, buff=0)

        tims_text50 = square_text_box('50', PURPLE_A, TEAL_A)
        tims_text50.next_to(tims_text4, buff=0)

        tims_text21 = square_text_box('21', PURPLE_A, TEAL_A)
        tims_text21.next_to(tims_text50, buff=0)

        tims_text8 = square_text_box('8', PURPLE_A, TEAL_A)
        tims_text8.next_to(tims_text21, buff=0)

        tims_text_right = MarkupText(r'<span font_family="monospace"><b>TimSort</b></span>', 
                                    color=TEAL_A)

        tims_text_right.shift(3.2 * DOWN + 4.5 * RIGHT)

        self.play(GrowFromCenter(tims_text41), GrowFromCenter(tims_text9), GrowFromCenter(tims_text3),GrowFromCenter(tims_text25),
                  GrowFromCenter(tims_text47),GrowFromCenter(tims_text19), GrowFromCenter(tims_text39), GrowFromCenter(tims_text28),
                  GrowFromCenter(tims_text4), GrowFromCenter(tims_text50), GrowFromCenter(tims_text21),GrowFromCenter(tims_text8), 
                  Write(tims_text_right))


        #  ------------step 1 ------------------------- 

        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 1</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        bubs_fill_box1 = square_swap(BLUE_D)
        bubs_fill_box1.shift(3 * UP, 6 * LEFT)

        bubs_fill_box2 = square_swap(BLUE_D)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text41, bubs_text9))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        sels_fill_box1 = square_swap(GOLD_C)
        sels_fill_box1.shift(1.8 * UP, 6 * LEFT)

        sels_fill_box2 = square_swap(GOLD_C)
        sels_fill_box2.next_to(sels_text9, buff=0)

        self.play(FadeIn(sels_fill_box1), FadeIn(sels_fill_box2))
        self.play(CyclicReplace(sels_text41, sels_text3))
        self.play(FadeOut(sels_fill_box1), FadeOut(sels_fill_box2))


        inss_fill_box1 = square_swap(TEAL_D)
        inss_fill_box1.shift(0.6 * UP, 6 * LEFT)

        inss_fill_box2 = square_swap(TEAL_D)
        inss_fill_box2.next_to(inss_text41, buff=0)

        self.play(FadeIn(inss_fill_box1), FadeIn(inss_fill_box2))
        self.play(CyclicReplace(inss_text41, inss_text9))
        self.play(FadeOut(inss_fill_box1), FadeOut(inss_fill_box2))


        mers_fill_box1 = square_swap(YELLOW_C)
        mers_fill_box1.shift(0.8 * DOWN, 6 * LEFT)

        mers_fill_box2 = square_swap(YELLOW_C)
        mers_fill_box2.next_to(mers_text41, buff=0)

        self.play(FadeIn(mers_fill_box1), FadeIn(mers_fill_box2))
        self.play(CyclicReplace(mers_text41, mers_text9))
        self.play(FadeOut(mers_fill_box1), FadeOut(mers_fill_box2))


        quis_fill_box1 = square_swap(MAROON_C)
        quis_fill_box1.next_to(quis_text19, buff=0)

        quis_fill_box2 = square_swap(MAROON_C)
        quis_fill_box2.next_to(quis_text47, buff=0)

        self.play(FadeIn(quis_fill_box1), FadeIn(quis_fill_box2))
        self.play(CyclicReplace(quis_text4, quis_text47))
        self.play(FadeOut(quis_fill_box1), FadeOut(quis_fill_box2))


        tims_fill_box1 = square_swap(PURPLE_A)
        tims_fill_box1.shift(3.2 * DOWN, 6 * LEFT)

        tims_fill_box2 = square_swap(PURPLE_A)
        tims_fill_box2.next_to(tims_text41, buff=0)

        self.play(FadeIn(tims_fill_box1), FadeIn(tims_fill_box2))
        self.play(CyclicReplace(tims_text41, tims_text9))
        self.play(FadeOut(tims_fill_box1), FadeOut(tims_fill_box2))

        #  ------------ step 2 ----------

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 2</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        bubs_fill_box1.next_to(bubs_text9, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        sels_fill_box1.next_to(sels_text3, buff=0)
        sels_fill_box2.next_to(sels_text47, buff=0)


        inss_fill_box3 = square_swap(TEAL_D)
        inss_fill_box3.shift(0.6 * UP, 6 * LEFT)
        inss_fill_box2.next_to(inss_text9, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)


        mers_fill_box3 = square_swap(YELLOW_C)
        mers_fill_box3.shift(0.8 * DOWN, 6 * LEFT)
        mers_fill_box2.next_to(mers_text9, buff=0)
        mers_fill_box1.next_to(mers_text41, buff=0)

        quis_fill_box1.next_to(quis_text50, buff=0)
        quis_fill_box2.next_to(quis_text4, buff=0)

        tims_fill_box3 = square_swap(PURPLE_A)
        tims_fill_box3.shift(3.2 * DOWN, 6 * LEFT)
        tims_fill_box2.next_to(tims_text9, buff=0)
        tims_fill_box1.next_to(tims_text41, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(sels_fill_box1), FadeIn(sels_fill_box2), 
            FadeIn(inss_fill_box1), FadeIn(inss_fill_box2), FadeIn(inss_fill_box3),FadeIn(mers_fill_box1), FadeIn(mers_fill_box2), 
            FadeIn(mers_fill_box3), FadeIn(quis_fill_box1), FadeIn(quis_fill_box2),FadeIn(tims_fill_box1), FadeIn(tims_fill_box2), FadeIn(tims_fill_box3))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text41, bubs_text3), CyclicReplace(sels_text9, sels_text4), 
            CyclicReplace(inss_text3, inss_text9, inss_text41), 
            CyclicReplace(mers_text3, mers_text9, mers_text41), CyclicReplace(quis_text21, quis_text47), 
            CyclicReplace(tims_text3, tims_text9, tims_text41))
        self.wait(0.2)
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(sels_fill_box1), FadeOut(sels_fill_box2),FadeOut(inss_fill_box1), 
            FadeOut(inss_fill_box2), FadeOut(inss_fill_box3), FadeOut(mers_fill_box1), FadeOut(mers_fill_box2), FadeOut(mers_fill_box3),
            FadeOut(quis_fill_box1), FadeOut(quis_fill_box2), FadeOut(tims_fill_box1), FadeOut(tims_fill_box2), FadeOut(tims_fill_box3))

        # --- step3 --

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 3</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        tims_fill_box1.next_to(tims_text9, buff=0)
        tims_fill_box2.next_to(tims_text41, buff=0)

        quis_fill_box1.next_to(quis_text21, buff=0)
        quis_fill_box2.next_to(quis_text47, buff=0)

        mers_fill_box3.next_to(mers_text25, buff=0)
        mers_fill_box2.next_to(mers_text9, buff=0)
        mers_fill_box1.next_to(mers_text41, buff=0)
        mers_fill_box4 = square_swap(YELLOW_C)
        mers_fill_box4.next_to(mers_text28, buff=0)


        inss_fill_box2.next_to(inss_text9, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)


        sels_fill_box1.next_to(sels_text4, buff=0)
        sels_fill_box2.next_to(sels_text21, buff=0)


        bubs_fill_box1.next_to(bubs_text3, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(sels_fill_box1), FadeIn(sels_fill_box2), FadeIn(inss_fill_box1), 
                  FadeIn(inss_fill_box2), FadeIn(mers_fill_box1), FadeIn(mers_fill_box2), FadeIn(mers_fill_box3), FadeIn(mers_fill_box4),
                  FadeIn(quis_fill_box1), FadeIn(quis_fill_box2), FadeIn(tims_fill_box1), FadeIn(tims_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text41, bubs_text25), CyclicReplace(sels_text41, sels_text8), CyclicReplace(inss_text25, inss_text41),
                  CyclicReplace( mers_text41, mers_text39, mers_text28, mers_text25), CyclicReplace(quis_text8, quis_text50), 
                  CyclicReplace(tims_text41, tims_text25))
        self.wait(0.2)
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(sels_fill_box1), FadeOut(sels_fill_box2), 
                  FadeOut(inss_fill_box1), FadeOut(inss_fill_box2), FadeOut(mers_fill_box1), FadeOut(mers_fill_box2), 
                  FadeOut(mers_fill_box3), FadeOut(mers_fill_box4), FadeOut(quis_fill_box1), FadeOut(quis_fill_box2),
                  FadeOut(tims_fill_box1), FadeOut(tims_fill_box2))



        # ------- step4 -----

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 4</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)





        bubs_fill_box1.next_to(bubs_text25, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        sels_fill_box1.next_to(sels_text8, buff=0)
        sels_fill_box2.next_to(sels_text47, buff=0)

        inss_fill_box2.next_to(inss_text25, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)


        mers_fill_box3.next_to(mers_text47, buff=0)
        mers_fill_box2.next_to(mers_text19, buff=0)
        mers_fill_box1.next_to(mers_text41, buff=0)


        quis_fill_box1 = square_swap(MAROON_C)
        quis_fill_box1.shift(2 * DOWN, 6 * LEFT)
        quis_fill_box2.next_to(quis_text21, buff=0)


        tims_fill_box1.next_to(tims_text25, buff=0)
        tims_fill_box2.next_to(tims_text41, buff=0)

        self.play(FadeIn(tims_fill_box1), FadeIn(tims_fill_box2), FadeIn(quis_fill_box1), FadeIn(quis_fill_box2),FadeIn(mers_fill_box1), 
                  FadeIn(mers_fill_box2), FadeIn(mers_fill_box3), FadeIn(inss_fill_box1), FadeIn(inss_fill_box2), FadeIn(sels_fill_box1), 
                  FadeIn(sels_fill_box2), FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(tims_text41, tims_text28), CyclicReplace(quis_text8, quis_text41), 
                  CyclicReplace(mers_text4, mers_text19, mers_text47), CyclicReplace(inss_text28, inss_text41), 
                  CyclicReplace(sels_text9, sels_text25), CyclicReplace(bubs_text41, bubs_text28))
        self.wait(0.2)
        self.play(FadeOut(tims_fill_box1), FadeOut(tims_fill_box2), FadeOut(quis_fill_box1), FadeOut(quis_fill_box2), 
                  FadeOut(mers_fill_box1), FadeOut(mers_fill_box2), FadeOut(mers_fill_box3), FadeOut(inss_fill_box1), FadeOut(inss_fill_box2), 
                  FadeOut(sels_fill_box1), FadeOut(sels_fill_box2), FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        # ---  step 5 ------

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 5</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)



        tims_fill_box1.next_to(tims_text28, buff=0)
        tims_fill_box2.next_to(tims_text41, buff=0)

        quis_fill_box1.next_to(quis_text8, buff=0)
        quis_fill_box2.next_to(quis_text9, buff=0)


        mers_fill_box2.next_to(mers_text47, buff=0)
        mers_fill_box1.next_to(mers_text50, buff=0)

        inss_fill_box2.next_to(inss_text28, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)

        sels_fill_box1.next_to(sels_text9, buff=0)
        sels_fill_box2.next_to(sels_text39, buff=0)


        bubs_fill_box1.next_to(bubs_text28, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(sels_fill_box1), FadeIn(sels_fill_box2), 
            FadeIn(inss_fill_box1), FadeIn(inss_fill_box2), FadeIn(mers_fill_box1), FadeIn(mers_fill_box2),
            FadeIn(quis_fill_box1), FadeIn(quis_fill_box2), FadeIn(tims_fill_box1), FadeIn(tims_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text41, bubs_text39), CyclicReplace(sels_text28, sels_text19), CyclicReplace(inss_text39, inss_text41),
            CyclicReplace(mers_text50, mers_text21), CyclicReplace(quis_text3, quis_text9), CyclicReplace(tims_text41, tims_text39))
        self.wait(0.2)
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(sels_fill_box1), FadeOut(sels_fill_box2), 
            FadeOut(inss_fill_box1), FadeOut(inss_fill_box2), FadeOut(mers_fill_box1), FadeOut(mers_fill_box2), 
            FadeOut(quis_fill_box1), FadeOut(quis_fill_box2), FadeOut(tims_fill_box1), FadeOut(tims_fill_box2))


        # ----- step 6 ---------

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 6</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        bubs_fill_box1.next_to(bubs_text39, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)


        sels_fill_box1.next_to(sels_text19, buff=0)
        sels_fill_box2.next_to(sels_text50, buff=0)


        inss_fill_box3.next_to(inss_text9, buff=0)
        inss_fill_box4 = square_swap(TEAL_D)
        inss_fill_box4.next_to(inss_text25, buff=0)
        inss_fill_box5 = square_swap(TEAL_D)
        inss_fill_box5.next_to(inss_text28, buff=0)
        inss_fill_box2.next_to(inss_text39, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)


        mers_fill_box3.next_to(mers_text47, buff=0)
        mers_fill_box2.next_to(mers_text50, buff=0)
        mers_fill_box1.next_to(mers_text21, buff=0)

        quis_fill_box1.next_to(quis_text3, buff=0)
        quis_fill_box2.next_to(quis_text19, buff=0)

        tims_fill_box3.next_to(tims_text25, buff=0)
        tims_fill_box2.next_to(tims_text9, buff=0)
        tims_fill_box1.next_to(tims_text41, buff=0)
        tims_fill_box4 = square_swap(PURPLE_A)
        tims_fill_box4.next_to(tims_text39, buff=0)
        tims_fill_box5 = square_swap(PURPLE_A)
        tims_fill_box5.next_to(tims_text28, buff=0)

        self.play(FadeIn(quis_fill_box1), FadeIn(quis_fill_box2), FadeIn(mers_fill_box1), FadeIn(mers_fill_box2), FadeIn(mers_fill_box3),FadeIn(inss_fill_box1), FadeIn(inss_fill_box2), FadeIn(inss_fill_box3),
                  FadeIn(inss_fill_box4), FadeIn(inss_fill_box5), FadeIn(sels_fill_box1), FadeIn(sels_fill_box2), FadeIn(bubs_fill_box1), 
                  FadeIn(bubs_fill_box2),FadeIn(tims_fill_box1), FadeIn(tims_fill_box2), FadeIn(tims_fill_box3), 
                  FadeIn(tims_fill_box4), FadeIn(tims_fill_box5))
        self.wait(0.7)
        self.play(CyclicReplace(quis_text4, quis_text9), CyclicReplace(mers_text8, mers_text21, mers_text50), 
            CyclicReplace(inss_text19, inss_text25, inss_text28, inss_text39, inss_text41), CyclicReplace(sels_text39, sels_text21), 
            CyclicReplace(bubs_text41, bubs_text19),CyclicReplace( tims_text19, tims_text25, tims_text28, tims_text39, tims_text41))
        self.wait(0.2)
        self.play(FadeOut(quis_fill_box1), FadeOut(quis_fill_box2), FadeOut(mers_fill_box1), FadeOut(mers_fill_box2), FadeOut(mers_fill_box3), FadeOut(inss_fill_box1), FadeOut(inss_fill_box2), FadeOut(inss_fill_box3), 
                  FadeOut(inss_fill_box4), FadeOut(inss_fill_box5),FadeOut(sels_fill_box1), FadeOut(sels_fill_box2),FadeOut(bubs_fill_box1), 
                  FadeOut(bubs_fill_box2), FadeOut(tims_fill_box1), FadeOut(tims_fill_box2), FadeOut(tims_fill_box3), 
                  FadeOut(tims_fill_box4), FadeOut(tims_fill_box5))


        # -------- step 7 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 7</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        quis_fill_box1 = square_swap(MAROON_C)
        quis_fill_box1.shift(2 * DOWN, 6 * LEFT)
        quis_fill_box2.next_to(quis_text3, buff=0)

        tims_fill_box3.next_to(tims_text25, buff=0)
        tims_fill_box2.next_to(tims_text9, buff=0)
        tims_fill_box1.next_to(tims_text41, buff=0)
        tims_fill_box4.next_to(tims_text39, buff=0)
        tims_fill_box5.next_to(tims_text28, buff=0)

        tims_fill_box6 = square_swap(PURPLE_A)
        tims_fill_box6.next_to(tims_text3, buff=0)
        tims_fill_box7 = square_swap(PURPLE_A)
        tims_fill_box7.next_to(tims_text47, buff=0)
        tims_fill_box8 = square_swap(PURPLE_A)
        tims_fill_box8.next_to(tims_text19, buff=0)

        mers_fill_box3.next_to(mers_text4, buff=0)
        mers_fill_box2.next_to(mers_text19, buff=0)
        mers_fill_box1.next_to(mers_text47, buff=0)
        mers_fill_box4.next_to(mers_text8, buff=0)

        inss_fill_box3.next_to(inss_text9, buff=0)
        inss_fill_box4.next_to(inss_text25, buff=0)
        inss_fill_box5.next_to(inss_text28, buff=0)
        inss_fill_box2.next_to(inss_text39, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)

        inss_fill_box6 = square_swap(TEAL_D)
        inss_fill_box6.next_to(inss_text19, buff=0)

        inss_fill_box7 = square_swap(TEAL_D)
        inss_fill_box7.next_to(inss_text47, buff=0)

        inss_fill_box8 = square_swap(TEAL_D)
        inss_fill_box8.next_to(inss_text3, buff=0)


        sels_fill_box1.next_to(sels_text21, buff=0)
        sels_fill_box2.next_to(sels_text47, buff=0)

        bubs_fill_box1.next_to(bubs_text41, buff=0)
        bubs_fill_box2.next_to(bubs_text47, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2),FadeIn(inss_fill_box1), FadeIn(inss_fill_box2), FadeIn(inss_fill_box3),
                  FadeIn(inss_fill_box4), FadeIn(inss_fill_box5),
                  FadeIn(inss_fill_box6), FadeIn(inss_fill_box7), FadeIn(inss_fill_box8),FadeIn(sels_fill_box1), FadeIn(sels_fill_box2),FadeIn(mers_fill_box1), 
                  FadeIn(mers_fill_box2), FadeIn(mers_fill_box3), FadeIn(mers_fill_box4),FadeIn(tims_fill_box1), FadeIn(tims_fill_box2), FadeIn(tims_fill_box3), FadeIn(tims_fill_box8),
                  FadeIn(tims_fill_box4), FadeIn(tims_fill_box5), FadeIn(tims_fill_box6), FadeIn(tims_fill_box7),FadeIn(quis_fill_box1), FadeIn(quis_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text47, bubs_text4),CyclicReplace(sels_text28, sels_text25),
            CyclicReplace(inss_text4, inss_text9,  inss_text19, inss_text25, inss_text28, inss_text39, inss_text41,
                                 inss_text47),CyclicReplace( mers_text8, mers_text19, mers_text47, mers_text21),
            CyclicReplace( tims_text4, tims_text9,tims_text19, tims_text25, tims_text28, tims_text39, tims_text41, tims_text47),
            CyclicReplace(quis_text4, quis_text8))
        self.wait(0.2)
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(sels_fill_box1), FadeOut(sels_fill_box2),FadeOut(inss_fill_box1), FadeOut(inss_fill_box2), FadeOut(inss_fill_box3), 
                  FadeOut(inss_fill_box4), FadeOut(inss_fill_box5),
                  FadeOut(inss_fill_box6), FadeOut(inss_fill_box7), FadeOut(inss_fill_box8),FadeOut(mers_fill_box1), 
                  FadeOut(mers_fill_box2), FadeOut(mers_fill_box3), FadeOut(mers_fill_box4),FadeOut(tims_fill_box1), FadeOut(tims_fill_box2), FadeOut(tims_fill_box3), FadeOut(tims_fill_box8), 
                  FadeOut(tims_fill_box4), FadeOut(tims_fill_box5), FadeOut(tims_fill_box6), FadeOut(tims_fill_box7),FadeOut(quis_fill_box1), FadeOut(quis_fill_box2))


        # -------- step 8 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 8</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        tims_fill_box3.next_to(tims_text25, buff=0)
        tims_fill_box2.next_to(tims_text19, buff=0)
        tims_fill_box1.next_to(tims_text41, buff=0)
        tims_fill_box4.next_to(tims_text39, buff=0)
        tims_fill_box5.next_to(tims_text28, buff=0)
        tims_fill_box6.next_to(tims_text50, buff=0)
        tims_fill_box7.next_to(tims_text47, buff=0)

        quis_fill_box1 = square_swap(MAROON_C)
        quis_fill_box1.shift(2 * DOWN, 6 * LEFT)
        quis_fill_box2.next_to(quis_text4, buff=0)


        mers_fill_box3.next_to(mers_text9, buff=0)
        mers_fill_box4.next_to(mers_text25, buff=0)
        mers_fill_box5 = square_swap(YELLOW_C)
        mers_fill_box5.next_to(mers_text28, buff=0)
        mers_fill_box2.next_to(mers_text39, buff=0)
        mers_fill_box1.next_to(mers_text41, buff=0)
        mers_fill_box6 = square_swap(YELLOW_C)
        mers_fill_box6.next_to(mers_text19, buff=0)
        mers_fill_box7 = square_swap(YELLOW_C)
        mers_fill_box7.next_to(mers_text3, buff=0)
        mers_fill_box8 = square_swap(YELLOW_C)
        mers_fill_box8.next_to(mers_text4, buff=0)

        mers_fill_box9 = square_swap(YELLOW_C)
        mers_fill_box9.next_to(mers_text8, buff=0)


        inss_fill_box4.next_to(inss_text25, buff=0)
        inss_fill_box5.next_to(inss_text28, buff=0)
        inss_fill_box2.next_to(inss_text39, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)

        inss_fill_box6 = square_swap(TEAL_D)
        inss_fill_box6.next_to(inss_text19, buff=0)

        inss_fill_box7 = square_swap(TEAL_D)
        inss_fill_box7.next_to(inss_text47, buff=0)

        inss_fill_box8 = square_swap(TEAL_D)
        inss_fill_box8.next_to(inss_text50, buff=0)


        sels_fill_box1.next_to(sels_text25, buff=0)
        sels_fill_box2.next_to(sels_text47, buff=0)

        bubs_fill_box1.next_to(bubs_text47, buff=0)
        bubs_fill_box2.next_to(bubs_text50, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(sels_fill_box1), FadeIn(sels_fill_box2),FadeIn(inss_fill_box1), FadeIn(inss_fill_box2),
                  FadeIn(inss_fill_box4), FadeIn(inss_fill_box5),
                  FadeIn(inss_fill_box6), FadeIn(inss_fill_box7), FadeIn(inss_fill_box8),FadeIn(mers_fill_box1), FadeIn(mers_fill_box2), FadeIn(mers_fill_box3),
                  FadeIn(mers_fill_box4), FadeIn(mers_fill_box5), FadeIn(mers_fill_box9),
                  FadeIn(mers_fill_box6), FadeIn(mers_fill_box7), FadeIn(mers_fill_box8),FadeIn(quis_fill_box1), FadeIn(quis_fill_box2),FadeIn(tims_fill_box1), FadeIn(tims_fill_box2), FadeIn(tims_fill_box3),
                  FadeIn(tims_fill_box4), FadeIn(tims_fill_box5), FadeIn(tims_fill_box6), FadeIn(tims_fill_box7))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text50, bubs_text21),CyclicReplace(sels_text28, sels_text47),
            CyclicReplace(inss_text21, inss_text25, inss_text28, inss_text39, inss_text41,inss_text47,inss_text50),CyclicReplace(mers_text4, mers_text9, mers_text28,mers_text8, mers_text25), 
                  CyclicReplace(mers_text19, mers_text39),
                  CyclicReplace(mers_text41,mers_text21),CyclicReplace(quis_text4, quis_text3),
                  CyclicReplace( tims_text21, tims_text25, tims_text28, tims_text39, tims_text41, tims_text47, tims_text50))
        self.wait(0.2)
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2),FadeOut(sels_fill_box1), FadeOut(sels_fill_box2),FadeOut(inss_fill_box1), FadeOut(inss_fill_box2), 
                  FadeOut(inss_fill_box4), FadeOut(inss_fill_box5),
                  FadeOut(inss_fill_box6), FadeOut(inss_fill_box7), FadeOut(inss_fill_box8),FadeOut(mers_fill_box1), FadeOut(mers_fill_box2), FadeOut(mers_fill_box3), 
                  FadeOut(mers_fill_box4), FadeOut(mers_fill_box5), FadeOut(mers_fill_box9),
                  FadeOut(mers_fill_box6), FadeOut(mers_fill_box7), FadeOut(mers_fill_box8),FadeOut(quis_fill_box1), FadeOut(quis_fill_box2),FadeOut(tims_fill_box1), FadeOut(tims_fill_box2), FadeOut(tims_fill_box3),
                  FadeOut(tims_fill_box4), FadeOut(tims_fill_box5), FadeOut(tims_fill_box6), FadeOut(tims_fill_box7))

        framebox1 = SurroundingRectangle(merss_text_right, buff = .1)
        self.play(ShowCreation(framebox1))
        merss_sorted_stepn = MarkupText(r'<span font_family="monospace"><b>Sorted in 8 Steps</b></span>', 
                                    color=PURPLE_A).scale(0.25)
        merss_sorted_stepn.shift(1.4 * DOWN + 4.5 * RIGHT)
        self.play(Write(merss_sorted_stepn))
        framebox2 = SurroundingRectangle(merss_sorted_stepn, buff = .1)
        self.play(ShowCreation(framebox2))



        # -------- step 9 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 9</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)

        tims_fill_box3.next_to(tims_text25, buff=0)
        tims_fill_box2.next_to(tims_text9, buff=0)
        tims_fill_box1.next_to(tims_text41, buff=0)
        tims_fill_box4.next_to(tims_text39, buff=0)
        tims_fill_box5.next_to(tims_text28, buff=0)
        tims_fill_box6.next_to(tims_text50, buff=0)
        tims_fill_box7.next_to(tims_text47, buff=0)
        tims_fill_box8.next_to(tims_text19, buff=0)

        tims_fill_box9 = square_swap(PURPLE_A)
        tims_fill_box9.next_to(tims_text4, buff=0)
        tims_fill_box10 = square_swap(PURPLE_A)
        tims_fill_box10.next_to(tims_text21, buff=0)

        quis_fill_box1.next_to(quis_text25, buff=0)
        quis_fill_box2.next_to(quis_text39, buff=0)


        inss_fill_box3.next_to(inss_text9, buff=0)
        inss_fill_box4.next_to(inss_text25, buff=0)
        inss_fill_box5.next_to(inss_text28, buff=0)
        inss_fill_box2.next_to(inss_text39, buff=0)
        inss_fill_box1.next_to(inss_text41, buff=0)
        inss_fill_box6.next_to(inss_text19, buff=0)
        inss_fill_box7.next_to(inss_text47, buff=0)
        inss_fill_box8.next_to(inss_text4, buff=0)

        inss_fill_box9 = square_swap(TEAL_D)
        inss_fill_box9.next_to(inss_text50, buff=0)
        inss_fill_box10 = square_swap(TEAL_D)
        inss_fill_box10.next_to(inss_text21, buff=0)


        sels_fill_box1.next_to(sels_text28, buff=0)
        sels_fill_box2.next_to(sels_text50, buff=0)

        bubs_fill_box1.next_to(bubs_text21, buff=0)
        bubs_fill_box2.next_to(bubs_text50, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2),FadeIn(inss_fill_box1), FadeIn(inss_fill_box2), FadeIn(inss_fill_box3),
                  FadeIn(inss_fill_box4), FadeIn(inss_fill_box5), FadeIn(inss_fill_box9), FadeIn(inss_fill_box10),
                  FadeIn(inss_fill_box6), FadeIn(inss_fill_box7), FadeIn(inss_fill_box8),FadeIn(sels_fill_box1), FadeIn(sels_fill_box2),
                  FadeIn(quis_fill_box1), FadeIn(quis_fill_box2),FadeIn(tims_fill_box1), FadeIn(tims_fill_box2), FadeIn(tims_fill_box3), FadeIn(tims_fill_box8),
                  FadeIn(tims_fill_box4), FadeIn(tims_fill_box5), FadeIn(tims_fill_box6), FadeIn(tims_fill_box7),
                  FadeIn(tims_fill_box9), FadeIn(tims_fill_box10))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text50, bubs_text8),CyclicReplace(sels_text39, sels_text47),CyclicReplace(inss_text8, inss_text9, inss_text19,inss_text21, inss_text25, inss_text28, inss_text39, inss_text41,
                                 inss_text47, inss_text50),CyclicReplace(quis_text28, quis_text19),CyclicReplace( tims_text8, tims_text9,tims_text19, tims_text21, tims_text25, 
                                 tims_text28, tims_text39, tims_text41, tims_text47, tims_text50))
        self.wait(0.2)
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2),FadeOut(sels_fill_box1), FadeOut(sels_fill_box2),FadeOut(inss_fill_box1), FadeOut(inss_fill_box2), FadeOut(inss_fill_box3), 
                  FadeOut(inss_fill_box4), FadeOut(inss_fill_box5), FadeOut(inss_fill_box9), FadeOut(inss_fill_box10),
                  FadeOut(inss_fill_box6), FadeOut(inss_fill_box7), FadeOut(inss_fill_box8),FadeOut(quis_fill_box1), FadeOut(quis_fill_box2),FadeOut(tims_fill_box1), FadeOut(tims_fill_box2), FadeOut(tims_fill_box3), FadeOut(tims_fill_box8), 
                  FadeOut(tims_fill_box4), FadeOut(tims_fill_box5), FadeOut(tims_fill_box6), FadeOut(tims_fill_box7),
                  FadeOut(tims_fill_box9), FadeOut(tims_fill_box10))

        framebox1 = SurroundingRectangle(inss_text_right, buff = .1)
        self.play(ShowCreation(framebox1))
        inss_sorted_stepn = MarkupText(r'<span font_family="monospace"><b>Sorted in 9 Steps</b></span>', 
                                    color=GREEN_SCREEN).scale(0.25)
        inss_sorted_stepn.shift(0.1 * UP + 4.8 * RIGHT)
        self.play(Write(inss_sorted_stepn))
        framebox2 = SurroundingRectangle(inss_sorted_stepn, buff = .1)
        self.play(ShowCreation(framebox2))


        framebox1 = SurroundingRectangle(tims_text_right, buff = .1)
        self.play(ShowCreation(framebox1))
        tims_sorted_stepn = MarkupText(r'<span font_family="monospace"><b>Sorted in 9 Steps</b></span>', 
                                    color=TEAL_A).scale(0.25)
        tims_sorted_stepn.shift(3.73 * DOWN + 4.5 * RIGHT)
        self.play(Write(tims_sorted_stepn))
        framebox2 = SurroundingRectangle(tims_sorted_stepn, buff = .1)
        self.play(ShowCreation(framebox2))



        # -------- step 10 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 10</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        quis_fill_box1.next_to(quis_text28, buff=0)
        quis_fill_box2.next_to(quis_text19, buff=0)


        sels_fill_box1.next_to(sels_text39, buff=0)
        sels_fill_box2.next_to(sels_text47, buff=0)

        bubs_fill_box1 = square_swap(BLUE_D)
        bubs_fill_box1.shift(3 * UP, 6 * LEFT)
        bubs_fill_box2.next_to(bubs_text9, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(sels_fill_box1), FadeIn(sels_fill_box2), 
            FadeIn(quis_fill_box1), FadeIn(quis_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text3, bubs_text9), CyclicReplace(sels_text50, sels_text41),CyclicReplace(quis_text39, quis_text9))
        self.wait(0.2)
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2),FadeOut(quis_fill_box1), FadeOut(quis_fill_box2),
            FadeOut(sels_fill_box1), FadeOut(sels_fill_box2))

        framebox1 = SurroundingRectangle(sels_text_right, buff = .1)
        self.play(ShowCreation(framebox1))
        sels_sorted_stepn = MarkupText(r'<span font_family="monospace"><b>Sorted in 10 Steps</b></span>', 
                                    color=BLUE_D).scale(0.25)
        sels_sorted_stepn.shift(1.27 * UP + 4.8 * RIGHT)
        self.play(Write(sels_sorted_stepn))
        framebox2 = SurroundingRectangle(sels_sorted_stepn, buff = .1)
        self.play(ShowCreation(framebox2))

        # -------- step 11 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 11</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)

        quis_fill_box1.next_to(quis_text39, buff=0)
        quis_fill_box2.next_to(quis_text9, buff=0)

        bubs_fill_box1.next_to(bubs_text28, buff=0)
        bubs_fill_box2.next_to(bubs_text39, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(quis_fill_box1), FadeIn(quis_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text39, bubs_text19), CyclicReplace(quis_text21, quis_text28))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(quis_fill_box1), FadeOut(quis_fill_box2))

        # -------- step 12 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 12</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)


        quis_fill_box1.next_to(quis_text8, buff=0)
        quis_fill_box2.next_to(quis_text9, buff=0)

        bubs_fill_box1.next_to(bubs_text39, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(quis_fill_box1), FadeIn(quis_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text41, bubs_text4), CyclicReplace(quis_text21, quis_text25))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(quis_fill_box1), FadeOut(quis_fill_box2))



        # -------- step 13 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 13</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)

        quis_fill_box1.next_to(quis_text8, buff=0)
        quis_fill_box2.next_to(quis_text19, buff=0)

        bubs_fill_box1.next_to(bubs_text41, buff=0)
        bubs_fill_box2.next_to(bubs_text47, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(quis_fill_box1), FadeIn(quis_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text47, bubs_text21), CyclicReplace(quis_text21, quis_text9))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(quis_fill_box1), FadeOut(quis_fill_box2))


        # -------- step 14 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 14</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)

        quis_fill_box1.next_to(quis_text25, buff=0)
        quis_fill_box2.next_to(quis_text39, buff=0)

        bubs_fill_box1.next_to(bubs_text21, buff=0)
        bubs_fill_box2.next_to(bubs_text47, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2), FadeIn(quis_fill_box1), FadeIn(quis_fill_box2))
        self.wait(0.7)
        self.play(CyclicReplace(bubs_text47, bubs_text8), CyclicReplace(quis_text28, quis_text39))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2), FadeOut(quis_fill_box1), FadeOut(quis_fill_box2))

        framebox1 = SurroundingRectangle(quis_text_right, buff = .1)
        self.play(ShowCreation(framebox1))
        quis_sorted_stepn = MarkupText(r'<span font_family="monospace"><b>Sorted in 14 Steps</b></span>', 
                                    color=GREEN_A).scale(0.25)
        quis_sorted_stepn.shift(2.6 * DOWN + 4.5 * RIGHT)
        self.play(Write(quis_sorted_stepn))
        framebox2 = SurroundingRectangle(quis_sorted_stepn, buff = .1)
        self.play(ShowCreation(framebox2))



        # -------- step 15 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 15</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)

        bubs_fill_box1.next_to(bubs_text25, buff=0)
        bubs_fill_box2.next_to(bubs_text28, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text28, bubs_text19))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        # -------- step 16 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 16</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text), run_time=0.5)

        bubs_fill_box1.next_to(bubs_text28, buff=0)
        bubs_fill_box2.next_to(bubs_text39, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text39, bubs_text4))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        # -------- step 17 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 17</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text39, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text41, bubs_text21))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        # -------- step 18 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 18</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text21, buff=0)
        bubs_fill_box2.next_to(bubs_text41, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text41, bubs_text8))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        # -------- step 19 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 19</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text9, buff=0)
        bubs_fill_box2.next_to(bubs_text25, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text25, bubs_text19))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        # -------- step 20 --------


        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 20</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text25, buff=0)
        bubs_fill_box2.next_to(bubs_text28, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text28, bubs_text4))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))


        #  --- 39-21

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 21</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text39, buff=0)
        bubs_fill_box2.next_to(bubs_text28, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text39, bubs_text21))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 39-8

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 22</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text39, buff=0)
        bubs_fill_box2.next_to(bubs_text21, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text39, bubs_text8))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 25-4

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 23</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text19, buff=0)
        bubs_fill_box2.next_to(bubs_text25, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text25, bubs_text4))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 21-28

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 24</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text25, buff=0)
        bubs_fill_box2.next_to(bubs_text28, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text21, bubs_text28))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 28-8

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 25</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text28, buff=0)
        bubs_fill_box2.next_to(bubs_text21, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text28, bubs_text8))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 19-4

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 26</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text9, buff=0)
        bubs_fill_box2.next_to(bubs_text19, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text19, bubs_text4))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 25-21
        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 27</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text19, buff=0)
        bubs_fill_box2.next_to(bubs_text25, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text25, bubs_text21))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 25-8
        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 28</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text25, buff=0)
        bubs_fill_box2.next_to(bubs_text21, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text25, bubs_text8))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 9-4
        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 29</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text9, buff=0)
        bubs_fill_box2.next_to(bubs_text3, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text9, bubs_text4))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 21-8

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 30</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text19, buff=0)
        bubs_fill_box2.next_to(bubs_text21, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text21, bubs_text8))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 19-8

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 31</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text19, buff=0)
        bubs_fill_box2.next_to(bubs_text9, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text19, bubs_text8))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        #  --- 9-8

        self.play(FadeOut(step_text))
        step_text = MarkupText(r'<span font_family="monospace"><b>STEP 32</b></span>', 
                                    color=WHITE).scale(0.6)
        step_text.shift(3.65 * UP + 2.5 * RIGHT)
        self.play(Write(step_text))

        bubs_fill_box1.next_to(bubs_text9, buff=0)
        bubs_fill_box2.next_to(bubs_text4, buff=0)

        self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
        self.play(CyclicReplace(bubs_text9, bubs_text8))
        self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))

        framebox1 = SurroundingRectangle(bubs_text_right, buff = .1)
        self.play(ShowCreation(framebox1))
        bubs_sorted_stepn = MarkupText(r'<span font_family="monospace"><b>Sorted in 32 Steps</b></span>', 
                                    color=GREEN_B).scale(0.25)
        bubs_sorted_stepn.shift(2.43 * UP + 5 * RIGHT)
        self.play(Write(bubs_sorted_stepn))
        framebox2 = SurroundingRectangle(bubs_sorted_stepn, buff = .1)
        self.play(ShowCreation(framebox2))



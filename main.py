import turtle as tu
class cvraman():


    def __init__(self):
        self.point1=[(128, 430), (128, 422), (130, 414), (133, 409), (134, 400), (136, 394), (137, 390), (139, 383), (143,378), (145, 374), (148, 369), (154, 364), (158, 358), (161, 354), (168, 350), (176, 348), (183, 346), (189, 343), (195, 339), (203, 336), (210, 336), (214, 333), (218, 329), (221, 323), (223, 319), (226, 316), (230, 313), (228, 307), (227, 302), (225, 297), (223, 292), (222, 288), (220, 285), (218, 282), (216, 279), (215, 276), (212, 272), (209, 272), (208, 269), (207, 265), (206, 261), (204, 257), (204, 253), (203, 250), (202, 247), (202, 243), (202, 239), (203, 235), (204, 232), (206, 230), (210, 229), (211, 227), (212, 221), (212, 215), (211, 209), (212, 206), (214, 202), (215, 197), (217, 194), (218, 189),(220, 186), (224, 181), (228, 177), (232, 175), (236, 171), (241, 167), (246, 164), (250, 162), (255, 161), (257, 158), (259, 156)]
        self.point2=[(253, 160), (258, 157), (265, 158), (270, 162), (277, 164), (283, 168), (290, 171), (298, 174), (305,178), (311, 181), (318, 186), (325, 191), (329, 197), (332, 203), (337, 209), (341, 212), (343, 218), (347, 216), (352, 218), (356, 222), (357, 228), (354, 233), (354, 238), (351, 244), (351, 250), (348, 252), (348, 256), (349, 262), (346, 265), (344, 269), (340, 269), (339, 274), (336, 275), (336, 280), (335, 285), (334, 290), (334, 297), (338, 300), (341, 304), (342, 307), (345, 312), (349, 317), (353, 321), (358, 324), (363, 328), (370, 333), (376, 335), (382, 337), (387, 340), (392, 343), (397, 345), (402, 347), (407, 350), (411, 353), (416, 357), (421, 360), (425, 365), (431, 369), (433, 373), (436, 377),(437, 381), (441, 385)]
        self.point3=[(129, 424), (134, 428), (140, 431), (148, 433), (155, 434), (161, 434), (165, 433), (173, 436), (182,436), (191, 436), (201, 436), (210, 436), (220, 436), (229, 436), (241, 436), (249, 432), (258, 435), (265, 435), (272, 435), (285, 435), (298, 436), (310, 436), (318, 436), (327, 435), (337, 435), (345, 435), (353, 433), (363, 430), (373, 427), (380, 423), (390, 416), (396, 412), (402, 408), (410, 400), (416, 392), (420, 382), (423, 375), (424, 372)]
        self.point4=[(212, 228), (207, 228), (201, 229), (198, 225), (196, 220), (193, 216), (191, 212), (190, 208), (188,204), (187, 199), (187, 195), (184, 190), (184, 184), (185, 178), (182, 178), (181, 172), (181, 168), (184, 167), (184, 163), (187, 162), (191, 159), (193, 155), (195, 153), (200, 154), (206, 154), (212, 154), (218, 154), (224, 154), (231, 153), (236, 153), (241, 155), (250, 155), (255, 157), (263, 158), (271, 162), (280, 165), (286, 168), (294, 171), (306, 177), (311, 179), (309, 174), (307, 169), (301, 165), (295, 162), (290, 160), (284, 158), (278, 155), (271, 154), (266, 157), (268, 154), (274, 153), (281, 156), (288, 160), (296, 162), (300, 165), (307, 169), (313, 173), (316, 177), (321, 182), (325, 187),(330, 193), (333, 198), (336, 203), (339, 209), (340, 215), (344, 216), (350, 218), (353, 215), (353, 208), (356, 205), (357, 202), (357, 197), (354, 191), (353, 186), (349, 181), (346, 175), (342, 171), (338, 166), (334, 162), (329, 157), (325, 153), (319, 149), (314, 146), (308, 142), (304, 139), (298, 134), (293, 132), (288, 129), (284, 126), (280, 125), (274, 121), (274, 118), (276, 116), (285, 119), (293, 120), (299, 122), (304, 125), (307, 132), (312, 135), (319, 139), (325, 143), (332, 149), (338, 153), (343, 159), (349, 164), (352, 168), (355, 175), (357, 180), (358, 184), (360, 191), (360, 186), (364,185), (364, 181), (364, 177), (364, 172), (364, 169), (364, 164), (360, 164), (356, 161), (352, 158), (348, 153), (348, 147), (351, 151), (355, 154), (362, 160), (359, 157), (365, 160), (365, 158), (361, 156), (362, 152), (362, 148), (357, 145), (353, 142), (348, 139), (348, 143), (345, 144), (341, 141), (337, 139), (332, 136), (327, 133), (324, 129), (324, 125), (329, 128), (334, 130), (339, 135), (344, 136), (338, 132), (328, 127), (320, 123), (318, 119), (320, 123), (322, 126), (320, 130), (316, 128), (311, 126), (308, 124), (312, 127), (316, 127), (319, 127), (322, 123), (320, 120), (315, 115), (312, 112),(310, 108), (306, 105), (303, 103), (300, 101), (296, 99), (292, 99), (287, 99), (283, 99), (278, 97),(272, 95), (269, 95), (267, 95), (261, 98), (257, 102), (254, 105), (253, 108), (258, 110), (265, 111), (270, 113), (275, 115), (282, 117), (275, 114), (263, 110), (255, 109), (249, 109), (245, 111), (242,112), (238, 115), (234, 117), (229, 120), (224, 123), (220, 126), (215, 130), (210, 135), (206, 138), (205, 141), (202, 145), (200, 147), (198, 150), (199, 154), (207, 154), (215, 154), (221, 154), (229, 154), (237, 154), (242, 154), (248, 156), (255, 156), (258, 158), (263, 159), (270, 162), (279, 164), (285, 168), (294, 172), (301, 174), (308, 177), (316, 181), (321, 186), (328, 192), (335, 201), (343, 205), (348, 206), (350, 201), (349, 194), (344, 190), (344, 184), (338, 184), (333, 181), (342, 187), (341, 182), (338, 179), (336, 174), (333, 173), (329, 169), (326, 165), (324, 162), (321, 159), (317, 156),(314, 154), (311, 150), (316, 155), (321, 160), (328, 166), (325, 167), (319, 164), (315, 162), (311, 159), (308, 155), (304, 152), (300, 151), (296, 148), (290, 146), (286, 143), (280, 141), (276, 138), (271, 136), (266, 135), (260, 132), (254, 133), (249, 130), (245, 131), (241, 131), (246, 131), (255, 133), (263, 133), (268, 136), (276, 140), (283, 142), (292, 147), (298, 150), (305, 154), (313, 159), (319, 163), (323, 166), (332, 171), (338, 179), (339, 182), (345, 183), (346, 191), (352, 197), (350, 205), (355, 212), (352, 216), (344, 217), (341, 218), (342, 221), (346, 222), (344, 225), (345, 228), (346,233), (342, 234), (342, 239), (342, 241), (345, 246), (343, 248), (341, 253), (340, 258), (338, 262), (338, 266), (338, 271), (340, 259), (342, 253), (343, 249), (343, 244), (342, 237), (345, 229), (344, 223), (341, 218), (339, 210), (335, 203), (331, 196), (327, 191), (322, 186), (316, 182), (309, 177), (302, 176), (295, 172), (286, 168), (277, 164), (268, 160), (259, 157), (251, 154), (244, 154), (234, 153), (223, 152), (216, 151), (210, 153), (211, 161), (209, 165), (205, 170), (207, 167), (208, 165), (206, 163), (202, 166), (200, 169), (197, 171), (194, 176), (192, 181), (193, 185), (193, 191), (194, 197),(194, 203), (197, 209), (200, 213), (203, 217), (203, 220), (203, 217), (198, 212), (197, 206), (198, 201), (202, 196), (202, 193), (200, 192), (199, 185), (201, 178), (200, 182), (200, 189), (204, 195), (205, 190), (208, 184), (213, 181), (215, 178), (217, 174), (222, 172)]
        self.point5=[(231, 235), (235, 236), (240, 237), (244, 237), (248, 237), (251, 235), (254, 233), (254, 230), (257,228), (257, 225), (257, 222), (257, 219), (257, 216), (255, 214), (256, 212), (255, 211), (252, 209), (251, 208), (249, 206), (246, 206), (244, 206), (241, 206), (239, 207), (237, 207), (234, 207), (232, 209), (230, 211), (227, 211), (226, 213), (225, 216), (227, 216), (229, 214), (230, 213), (233, 212), (235, 210), (238, 210), (240, 209), (243, 210), (244, 208), (246, 210), (249, 210), (251, 208), (252, 210), (253, 209), (254, 208), (253, 207), (251, 208), (249, 209), (247, 209), (249, 208), (249, 208), (247, 207), (247, 209), (245, 209), (245, 208), (243, 209), (242, 208), (238, 208), (236, 208), (234, 208),(233, 211), (231, 211), (229, 211), (227, 212), (227, 214), (224, 215), (223, 218), (228, 215), (230, 210), (238, 209), (244, 208), (249, 208), (254, 209), (255, 213), (258, 218), (258, 222), (255, 223), (254, 225), (252, 227), (249, 228), (245, 229), (242, 231), (239, 230), (236, 229), (231, 229), (230, 227), (227, 226), (228, 224), (230, 222), (233, 220), (236, 219), (240, 219), (244, 220), (248, 223), (251, 226), (251, 225), (249, 224), (246, 222), (247, 225), (244, 225), (243, 225), (243, 227), (241, 227), (238, 229), (237, 227), (237, 225), (237, 222), (238, 220), (241, 220), (244, 221), (245, 223), (243,222), (242, 224), (241, 224), (241, 222), (239, 222), (240, 223), (240, 225), (238, 226), (238, 223), (240, 224), (240, 222), (244, 221)]
        self.point6=[(314, 226), (311, 230), (309, 232), (305, 233), (300, 233), (297, 234), (293, 234), (289, 232), (286,230), (282, 227), (279, 226), (279, 223), (276, 223), (274, 221), (273, 216), (272, 214), (274, 211), (275, 208), (277, 206), (279, 203), (282, 202), (285, 202), (289, 202), (294, 202), (300, 204), (304, 205), (308, 207), (306, 209), (302, 208), (300, 207), (297, 206), (293, 206), (291, 206), (288, 206), (285, 207), (283, 209), (280, 209), (276, 209), (275, 210), (272, 212), (272, 215), (272, 216), (272, 218), (275, 222), (277, 225), (281, 225), (283, 225), (287, 226), (290, 227), (293, 227), (297, 227), (301, 226), (304, 224), (307, 222), (309, 220), (307, 219), (306, 218), (304, 217), (302, 216), (301, 214),(298, 214), (295, 214), (297, 213), (295, 213), (292, 213), (289, 214), (286, 217), (284, 219), (282, 221), (282, 222), (281, 224), (284, 225), (287, 225), (291, 225), (294, 225), (293, 224), (291, 222), (291, 219), (292, 218), (294, 216), (296, 216), (299, 216), (302, 217), (303, 218), (303, 221), (303, 222), (302, 226), (302, 226), (301, 224), (300, 224), (299, 221), (299, 220), (299, 218), (298, 218), (296, 218), (297, 218), (297, 220), (294, 219), (294, 222), (296, 222), (298, 223), (295, 223), (293, 222), (297, 224), (297, 225)]
        self.point7=[(275, 213), (275, 217), (274, 221), (273, 225), (273, 230), (273, 237), (274, 241), (276, 245), (279,248), (282, 251), (285, 254), (288, 258), (287, 262), (286, 265), (285, 267), (282, 268), (279, 268), (276, 267), (273, 267), (271, 265), (274, 264), (277, 263), (279, 263), (283, 264), (286, 266), (284, 264), (281, 264), (277, 264), (273, 264), (272, 267), (268, 268), (266, 269), (264, 268), (264, 265), (262, 264), (261, 262), (259, 262), (257, 262), (253, 262), (249, 262), (249, 259), (250, 257), (254, 255), (254, 252), (255, 251), (252, 254), (250, 257), (250, 260), (252, 264), (252, 266), (255, 266), (257, 267), (259, 267), (262, 267), (264, 269), (269, 270), (270, 271), (271, 273), (271, 275), (272, 277),(272, 275), (269, 269), (267, 269), (265, 269), (265, 272), (265, 275), (265, 276)]
        self.point8=[(263, 230), (263, 235), (263, 241), (264, 240), (264, 236), (264, 234)]
        self.point9=[(247, 286), (252, 286), (252, 285), (254, 283), (257, 282), (261, 282), (265, 282), (269, 282), (270,282), (273, 280), (278, 280), (282, 279), (284, 281), (289, 281), (293, 282), (296, 282), (294, 284), (290, 283), (285, 283), (282, 282), (278, 282), (274, 282), (271, 282), (268, 284), (265, 285), (261, 284), (258, 284), (254, 284), (250, 285), (250, 289), (251, 290), (252, 292), (255, 293), (259, 293), (262, 293), (265, 293), (268, 295), (272, 295), (276, 294), (280, 293), (284, 292), (287, 291), (289, 290), (290, 288), (292, 287), (288, 286), (285, 286), (282, 286), (280, 287), (278, 286), (276, 286), (274, 286), (273, 286), (271, 287), (267, 287), (264, 288), (262, 287), (260, 287), (258, 287), (256, 287),(254, 287)]
        self.point10=[(266, 304), (269, 305), (271, 304), (274, 303), (277, 303), (273, 304), (268, 303), (265, 303), (262,302), (260, 302), (264, 303), (267, 304), (271, 301), (274, 301), (278, 303), (280, 301)]
        self.point11=[(166, 431), (167, 428), (170, 425), (171, 424), (171, 422), (171, 419), (173, 416), (176, 415), (177,412), (179, 408), (180, 406), (181, 403), (183, 400), (184, 396), (185, 405), (184, 412), (185, 407), (185, 403), (184, 395), (183, 393), (180, 392), (176, 389), (175, 386), (177, 383), (179, 379), (182, 375), (186, 371), (188, 366), (191, 362), (194, 355), (199, 350), (204, 344), (208, 339), (212, 337), (216, 335), (215, 340), (211, 347), (210, 353), (209, 358), (206, 364), (204, 370), (201, 374), (200, 379), (198, 383), (195, 387), (192, 390), (190, 392), (186, 394), (191, 390), (195, 386), (198, 380), (202, 372), (204, 366), (207, 360), (209, 355), (212, 348), (214, 343), (216, 335), (218, 329), (221, 325),(224, 321), (225, 316), (230, 311), (232, 318), (232, 323), (234, 326), (240, 334), (243, 338), (250, 343), (250, 346), (251, 351), (252, 355), (252, 360), (251, 363), (247, 364), (243, 361), (240, 357), (236, 353), (232, 350), (230, 346), (230, 340), (230, 333), (230, 329), (228, 326), (230, 337), (231, 353), (231, 360), (231, 367), (233, 376), (234, 382), (237, 388), (241, 397), (243, 403), (243, 408), (246, 414), (249, 418), (249, 422), (249, 428), (249, 432), (244, 430), (240, 425), (235, 421), (235, 416), (233, 412), (229, 406), (228, 400), (228, 394), (224, 390), (223, 381), (222, 373), (219, 369), (219,362), (219, 355), (220, 350), (220, 345), (220, 341), (218, 336), (219, 350), (220, 363), (218, 370), (218, 375), (218, 382), (217, 388), (219, 380), (219, 377), (224, 374), (224, 381), (224, 390), (222, 394), (221, 399), (221, 403), (221, 406), (222, 409), (223, 415), (222, 411), (221, 407), (220, 403), (220, 396), (223, 390), (227, 391), (228, 397), (231, 404), (233, 408), (235, 412), (239, 417), (241, 423), (247, 429), (249, 420), (249, 417), (251, 411), (252, 405), (255, 401), (255, 397), (257, 393), (260, 389), (262, 385), (262, 381), (263, 377), (263, 373), (263, 369), (258, 368), (255, 365), (250, 364),(253, 359), (254, 363), (258, 365), (260, 364), (263, 361), (265, 358), (268, 355), (272, 351), (272, 349), (268, 348), (265, 344), (262, 343), (261, 339), (258, 337), (254, 334), (252, 330), (248, 327), (244, 323), (240, 321), (236, 318), (234, 314), (238, 315), (242, 317), (247, 319), (251, 322), (255, 325), (260, 325), (265, 325), (269, 324), (274, 324), (276, 324), (281, 325), (284, 328), (279, 330), (274, 331), (271, 331), (278, 331), (282, 330), (288, 326), (289, 323), (293, 324), (297, 322), (294, 320), (298, 319), (304, 317), (307, 316), (307, 314), (310, 311), (313, 308), (317, 306), (320, 303), (323,298), (326, 294), (328, 290), (330, 287), (333, 284), (332, 291), (333, 295), (333, 299), (333, 301), (333, 305), (330, 306), (328, 309), (324, 313), (321, 317), (317, 321), (311, 324), (306, 326), (302, 328), (295, 330), (292, 335), (289, 337), (288, 343), (289, 347), (289, 350), (290, 357), (289, 359), (289, 362), (289, 365), (292, 361), (290, 354), (290, 347), (289, 339), (287, 336), (285, 338), (282, 341), (284, 337), (290, 340), (289, 347), (289, 357), (286, 359), (281, 356), (273, 351), (275, 346), (280, 342), (278, 345), (275, 353), (279, 356), (285, 357), (291, 365), (295, 362), (302, 361), (307, 359),(312, 357), (312, 362), (310, 366), (308, 371), (306, 375), (304, 379), (302, 384), (300, 388), (298, 394), (296, 398), (294, 402), (292, 407), (289, 411), (285, 421), (282, 427), (282, 421), (280, 415), (280, 409), (278, 403), (278, 397), (277, 389), (274, 384), (271, 384), (266, 384), (270, 384), (276, 383), (278, 377), (282, 373), (285, 371), (285, 369)]
        self.point12=[(290, 349), (294, 349), (297, 347), (302, 346), (305, 343), (309, 341), (313, 338), (317, 336), (319,334), (322, 330), (326, 328), (329, 325), (333, 319), (334, 312), (335, 307), (335, 303), (335, 313), (332, 322), (329, 331), (328, 335), (326, 338), (323, 343), (319, 349), (315, 357), (311, 365), (307, 373), (304, 380), (300, 385), (297, 393), (292, 404), (289, 412), (285, 420), (282, 429), (286, 430), (292, 429), (297, 427), (301, 423), (305, 418), (308, 414), (313, 404), (313, 398), (318, 394), (319, 388), (322, 386), (323, 381), (327, 378), (328, 375), (331, 370), (334, 366), (338, 365), (339, 369), (342, 374), (342, 370), (338, 369), (337, 363), (337, 358), (341, 357), (340, 354), (345, 354), (344, 350),(349, 349), (349, 343), (351, 337), (352, 333), (352, 327), (356, 325), (360, 328), (363, 333), (368, 336), (365, 341), (372, 343), (371, 349), (374, 354), (374, 359), (377, 365), (377, 370), (372, 371), (371, 363), (368, 361), (366, 354), (364, 351), (363, 345), (364, 353), (368, 360), (372, 367), (371, 372), (378, 372), (380, 380), (376, 381), (370, 382), (372, 386), (366, 387), (365, 389), (360, 389), (359, 394), (358, 399), (362, 399), (360, 404), (365, 402), (362, 407), (369, 406), (366, 412), (372, 412), (372, 418), (370, 420), (368, 421), (367, 423), (365, 423), (362, 423), (362, 427), (358, 426), (358,431), (353, 431), (351, 430)]
        self.point13=[(349, 223), (344, 224), (343, 228), (346, 233), (349, 236), (348, 242), (349, 247), (348, 253), (347,259), (346, 265), (342, 267), (338, 265), (338, 260), (339, 267), (343, 268), (346, 263), (347, 259), (347, 252), (344, 250), (342, 252), (340, 251), (340, 248), (340, 242), (340, 238), (340, 235), (341, 240), (344, 242), (345, 246), (346, 249), (347, 248), (350, 245), (350, 243), (354, 240), (354, 235), (348, 234), (343, 231), (342, 228)]
        self.point14=[(210, 227), (205, 227), (202, 227), (200, 232), (201, 235), (201, 237), (201, 242), (202, 244), (202,247), (202, 251), (203, 253), (205, 257), (208, 260), (209, 263), (210, 267), (210, 269), (213, 272), (215, 269), (217, 266), (215, 262), (215, 259), (212, 257), (213, 252), (212, 248), (213, 245), (213, 241), (213, 237), (210, 235), (206, 235), (206, 237), (207, 240), (207, 244), (207, 245), (207, 248), (206, 240), (206, 234), (205, 229), (203, 229), (202, 229), (199, 228), (199, 225), (196, 222), (197, 225), (202, 228), (208, 228), (213, 228), (211, 225), (211, 223)]
        self.point15=[(233, 311), (232, 308), (231, 305), (230, 303), (229, 300), (228, 297), (226, 295), (225, 292), (223, 289), (222, 286), (220, 284), (219, 280), (219, 278), (217, 275), (215, 273), (214, 271), (216, 269), (216, 265), (215, 261), (214, 259), (214, 257), (214, 254), (214, 251), (212, 246), (212, 242), (212, 238)]
        self.point16=[(275, 214), (275, 210), (276, 208), (278, 206), (280, 205), (283, 205), (286, 204), (288, 203), (291, 203), (294, 203), (296, 202), (298, 202), (299, 203), (301, 203), (304, 204), (306, 205), (306, 208), (305, 209), (305, 209), (305, 209), (307, 208), (305, 206), (305, 207), (302, 206), (301, 205), (297, 204), (295, 204), (292, 204), (288, 204), (285, 204), (283, 204), (280, 206), (278, 207), (276, 209), (278, 209), (280, 207), (282, 207), (284, 207), (286, 206), (288, 206), (291, 205), (292, 205), (294, 205), (297, 205), (299, 205), (301, 205), (303, 208), (301, 208), (300, 207), (292, 204), (293, 202), (291, 202), (290, 203), (287, 205), (287, 205), (289, 205), (286, 207), (283, 209), (280, 209), (279, 209), (277, 209), (277, 211), (280, 208), (289, 204), (296, 203), (302, 204), (304, 205), (306, 208), (309, 208), (310, 208), (309, 209)]
        self.point17=[(412, 357), (418, 360), (423, 364), (430, 370), (434, 374), (439, 379), (430, 381), (425, 387), (419,393), (414, 397), (411, 402), (407, 408)]
       
        



        self.pen = tu.Turtle()
        self.pen.pensize(5)        
        self.pen.hideturtle()

        self.pen.speed(10)

        self.x_offset = 300

        self.y_offset = 300

    def go(self, x, y):

        self.pen.penup()

        self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)

        self.pen.pendown()


#pencolor

    def paint(self,coord,):

        self.pen.color()

        t_x,t_y = coord[0]

        self.go(t_x,t_y)

        
        t = 0

        for i in coord[1:]:

            print(i)

            x,y = i

            if t:

                self.go(x,y)

                t = 0

                

                continue

            if x == -1 and y == -1:

                t = 1

                
                continue

            else:

                self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset) 

       
#for draw        

    def draw_fn(self,coord,mode = 1,thickness = 5):

        



        self.pen.color()



        if mode:

            self.pen.width(thickness)

            t_x,t_y = coord[0]

            self.go(t_x,t_y)

            t = 0

            for i in coord[1:]:

                print(i)

                x,y = i

                if t:

                    self.go(x,y)

                    t = 0

                    continue

                if x == -1 and y == -1:

                    t = 1

                    continue

                else:

                    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)

        else:

            self.paint(coord=coord)        

            

#what and how to draw

    def draw(self,retain=True):

        self.draw_fn(self.point1,mode = 0)

        self.draw_fn(self.point2,mode = 0)

        self.draw_fn(self.point3,mode = 0)
   
        self.draw_fn(self.point4,mode = 0)

        self.draw_fn(self.point5,mode = 0)

        self.draw_fn(self.point6,mode = 0)

        self.draw_fn(self.point7,mode = 0)

        self.draw_fn(self.point8,mode = 0)

        self.draw_fn(self.point9,mode = 0)

        self.draw_fn(self.point10,mode = 0)

        self.draw_fn(self.point11,mode = 0)

        self.draw_fn(self.point12,mode = 0)

        self.draw_fn(self.point13,mode = 0)

        self.draw_fn(self.point14,mode = 0)

        self.draw_fn(self.point15,mode = 0)

        self.draw_fn(self.point16,mode = 0)

        self.draw_fn(self.point17,mode = 0)

       


        


pen = cvraman()
tu.Screen().bgcolor("#008080")
tu.Screen().getcanvas().winfo_toplevel().attributes("-fullscreen", True) 



pen.draw() 
#to write name

tu.penup()
tu.goto(0, 270)
tu.color('#A8A9AD')
tu.write("NATIONAL SCIENCE DAY", align="center", font=("Verdana", 25, "bold"))


tu.goto(0, -270)
tu.color('#A8A9AD')
tu.write("SIR CHANDRASEKHARA VENKATA RAMAN", align="center", font=("Arial", 25, "bold"))
            
            
tu.done()


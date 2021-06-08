#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdarg.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <limits.h>
#include <time.h>

#include <GLFW/glfw3.h>

#define NK_INCLUDE_FIXED_TYPES
#define NK_INCLUDE_STANDARD_IO
#define NK_INCLUDE_STANDARD_VARARGS
#define NK_INCLUDE_DEFAULT_ALLOCATOR
#define NK_INCLUDE_VERTEX_BUFFER_OUTPUT
#define NK_INCLUDE_FONT_BAKING
#define NK_INCLUDE_DEFAULT_FONT
#define NK_IMPLEMENTATION
#define NK_GLFW_GL2_IMPLEMENTATION
#define NK_KEYSTATE_BASED_INPUT
#include "nuklear.h"
#include "nuklear_glfw_gl2.h"

#define WINDOW_WIDTH 1200
#define WINDOW_HEIGHT 800

#define INCLUDE_OVERVIEW

// #include "../calculator.c"

static void error_callback(int e, const char *d)
{printf("Error %d: %s\n", e, d);}

int main(void)
{
    /* Platform */
    static GLFWwindow *win;
    int width = 0, height = 0;
    struct nk_context *ctx;
    struct nk_colorf bg;

    /* GLFW */
    glfwSetErrorCallback(error_callback);
    if (!glfwInit()) {
        fprintf(stdout, "[GFLW] failed to init!\n");
        exit(1);
    }
    win = glfwCreateWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "Demo", NULL, NULL);
    glfwMakeContextCurrent(win);
    glfwGetWindowSize(win, &width, &height);

    /* GUI */
    ctx = nk_glfw3_init(win, NK_GLFW3_INSTALL_CALLBACKS);
    /* Load Fonts: if none of these are loaded a default font will be used  */
    /* Load Cursor: if you uncomment cursor loading please hide the cursor */
    {
	    struct nk_font_atlas *atlas;
	    nk_glfw3_font_stash_begin(&atlas);

	    nk_glfw3_font_stash_end();
    }

    bg.r = 0.10f, bg.g = 0.18f, bg.b = 0.24f, bg.a = 1.0f;
    while (!glfwWindowShouldClose(win))
    {
   	    glfwGetWindowSize(win, &width, &height);
        /* Input */
        glfwPollEvents();
        nk_glfw3_new_frame();

        if (nk_begin(ctx, "Calculator", nk_rect(0, 0, width, height), 0))
        {
            static int set = 0, prev = 0, op = 0;
            int index_a, index_b;
            // int
            static const char numbers[] = "789456123";
            static const char ops[] = "+-*/";
            static int a = 0, b = 0;
            static int *current = &a;
              char _a[200];
              char _b[200];
              char _output[40000];
              // char *_current = &_a;

            size_t i = 0;
            int solve = 0;
            {int len; char buffer[40000];
            nk_layout_row_dynamic(ctx, height / 5, 1);
            len = snprintf(buffer, 256, "%d", *current);
            nk_edit_string(ctx, NK_EDIT_SIMPLE, buffer, &len, 255, nk_filter_float);
            buffer[len] = 0;
            *current = atof(buffer);}

            nk_layout_row_dynamic(ctx, height / 5 - 10, 4);
            for (i = 0; i < 16; ++i) {
                if (i >= 12 && i < 15) {
                    if (i > 12) continue;
                    if (nk_button_label(ctx, "C")) {
                        a = b = op = 0; current = &a; set = 0;
                        for (int x = 0; x<200; x++){
                          _a[x] = 0;
                          _b[x] = 0;
                        }
                    } if (nk_button_label(ctx, "0")) {
                        *current = *current*10.0f;
                        set = 0;
                        if (current == &b) {
                          if(index_b>=200)break;
                            _b[index_b]= 0;
                            index_b++;
                        } else {
                          if(index_a>=200)break;
                            _a[index_a]= 0;
                            index_a++;
                        }
                    } if (nk_button_label(ctx, "=")) {
                        solve = 1; prev = op; op = 0;
                        for (int x = 0; x<200; x++){
                          printf("%c ->", _a[x]);
                        }
                        printf("\n");
                    }
                } else if (((i+1) % 4)) {
                    if (nk_button_text(ctx, &numbers[(i/4)*3+i%4], 1)) {
                        *current = *current * 10.0f + numbers[(i/4)*3+i%4] - '0';
                        if (current == &b) {
                          if(index_b>=200)break;
                            _b[index_b]= numbers[(i/4)*3+i%4];
                            index_b++;
                        } else {
                          if(index_a>=200)break;
                            _a[index_a]= numbers[(i/4)*3+i%4];
                            index_a++;
                        }
                        set = 0;
                    }
                } else if (nk_button_text(ctx, &ops[i/4], 1)) {
                    if (!set) {
                        if (current != &b) {
                            current = &b;
                        } else {
                            prev = op;
                            solve = 1;
                        }
                    }
                    op = ops[i/4];
                    set = 1;
                }
            }
            if (solve) {
                if (prev == '+') a = a + b;
                if (prev == '-') a = a - b;
                if (prev == '*') a = a * b;
                if (prev == '/') a = a / b;
                current = &a;
                if (set) current = &b;
                b = 0; set = 0;
            }
        }
        nk_end(ctx);

        /* Draw */
        glfwGetWindowSize(win, &width, &height);
        glViewport(0, 0, width, height);
        glClear(GL_COLOR_BUFFER_BIT);
        glClearColor(bg.r, bg.g, bg.b, bg.a);
        /* IMPORTANT: `nk_glfw_render` modifies some global OpenGL state
         * with blending, scissor, face culling and depth test and defaults everything
         * back into a default state. Make sure to either save and restore or
         * reset your own state after drawing rendering the UI. */
        nk_glfw3_render(NK_ANTI_ALIASING_ON);
        glfwSwapBuffers(win);
    }
    nk_glfw3_shutdown();
    glfwTerminate();
    return 0;
}

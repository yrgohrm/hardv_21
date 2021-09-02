struct rectangle {
    int height;
    int width;
};

int rectangle_area(struct rectangle *r) {
    return r->height * r->width;
}

int main() {
    struct rectangle rect1;
    rect1.height = 10;
    rect1.width = 20;

    struct rectangle rect2;
    rect2.height = 33;
    rect2.width = 45;

    printf("%d\n", rectangle_area(&rect1));
    printf("%d\n", rectangle_area(&rect2));
}
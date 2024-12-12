#include <iostream>
#include <pthread.h>

// Стэк нодыг тодорхойлох бүтэц
struct StackNode {
    int data;
    StackNode* next;
};

// Дэлхийн хувьсагчид
StackNode* top = NULL; // Стэкийн эхний заалт
pthread_mutex_t mutex; // Mutex lock

// Функцийн прототипууд
void* testStack(void* arg);
void push(int data);
int pop();

int main() {
    // Mutex lock-ийг эхлүүлэх
    if (pthread_mutex_init(&mutex, NULL) != 0) {
        std::cerr << "Mutex эхлүүлэхэд алдаа гарлаа" << std::endl;
        return 1;
    }

    // 200 thread үүсгэх
    pthread_t threads[200];
    for (int i = 0; i < 200; ++i) {
        if (pthread_create(&threads[i], NULL, testStack, NULL) != 0) {
            std::cerr << "Thread үүсгэхэд алдаа гарлаа" << std::endl;
            return 1;
        }
    }

    // Бүх thread-уудыг нэгдэх
    for (int i = 0; i < 200; ++i) {
        if (pthread_join(threads[i], NULL) != 0) {
            std::cerr << "Thread нэгдэхэд алдаа гарлаа" << std::endl;
            return 1;
        }
    }

    // Mutex lock-ийг устгах
    pthread_mutex_destroy(&mutex);

    return 0;
}

// testStack функц
void* testStack(void* arg) {
    // 3 push, 3 pop үйлдлийг давтан гүйцэтгэх
    for (int i = 0; i < 500; ++i) {
        if (i % 6 < 3) {
            // Push үйлдэл
            pthread_mutex_lock(&mutex); // Lock авах
            push(i);
            pthread_mutex_unlock(&mutex); // Lock-ийг суллах
        } else {
            // Pop үйлдэл
            pthread_mutex_lock(&mutex); // Lock авах
            int value = pop();
            pthread_mutex_unlock(&mutex); // Lock-ийг суллах
            // Pop утгыг ашиглах бол энд нэмнэ
        }
    }
    return NULL;
}

// Push үйлдэл
void push(int data) {
    // Шинэ node үүсгэх
    StackNode* newNode = new StackNode();
    newNode->data = data;
    newNode->next = top; // Өмнөх top руу заах

    // Top-ыг шинэ node руу шилжүүлэх
    top = newNode;
}

// Pop үйлдэл
int pop() {
    if (top == NULL) {
        std::cerr << "Стэк хоосон байна!" << std::endl;
        return -1; // Стэк хоосон бол алдаа өгнө
    }

    // Top элементийг хуулах
    StackNode* temp = top;
    int value = temp->data;
    top = top->next; // Top-ийг дараагийн элемент руу шилжүүлэх

    // Pop хийгдсэн node-г чөлөөлөх
    delete temp;

    return value;
}

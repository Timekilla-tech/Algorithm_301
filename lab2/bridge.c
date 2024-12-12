#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>  // for sleep()

// Синхрончлолын глобал хувьсагчид
sem_t flag_A, flag_B;
pthread_mutex_t bridge_mutex;

// Санамсаргүй байдлаар цаг үүсгэж байна
#define CROSSING_TIME (rand() % 5 + 1)  // 1-5-ийн хооронд

// Хойд талаас урагшаа
void* cross_from_A_to_B(void* arg) {
    sem_wait(&flag_A);  // Өөрийн талд туг ирэхийг хүлээнэ.
    printf("Хойд арлын фермер тугаа аван гүүр гаталж байна.\n");

    // Гүүрээр гарч байна
    sleep(CROSSING_TIME);

    // Гүүрээр гарсаны дараагаар тухайн талдаа тугаа байршуулна
    sem_post(&flag_B);
    printf("Хойд арлаас урд талын арал руу амжилттай гүүрээр гаран урд талд тугаа үлдээлээ.\n");

    return NULL;
}

void* cross_from_B_to_A(void* arg) {
    
    sem_wait(&flag_B);
    printf("Урд арлын фермер тугаа аван гүүр гаталж байна.\n");

    sleep(CROSSING_TIME);

    sem_post(&flag_A);
    printf("Урд арлаас хойд талын арал руу амжилттай гүүрээр гаран урд талд тугаа үлдээлээ.\n");

    return NULL;
}

int main() {
    srand(time(NULL)); // Санамсаргүйгээр тоо үүсгэж байна

    // Мутекс болон семафорыг хэрэгжүүлж байна
    pthread_mutex_init(&bridge_mutex, NULL);
    sem_init(&flag_A, 0, 1);  // Тугыг анхлан хойд талд байршуулна
    sem_init(&flag_B, 0, 0);  // Урд талд туг байхгүй

    // Урд болон хойд арлын тариачдадыг үүсгэх урсгалыг бий болгож байна
    pthread_t farmers[6];  // Аль аль талдаа 3 фермер байна.

    // Хойд арлын тариачид
    for (int i = 0; i < 3; i++) {
        pthread_create(&farmers[i], NULL, cross_from_A_to_B, NULL);
    }

    // Урд арлын
    for (int i = 3; i < 6; i++) {
        pthread_create(&farmers[i], NULL, cross_from_B_to_A, NULL);
    }

    // Бүх тариачдыг гүүрээр гарч дуусахыг хүлээнэ
    for (int i = 0; i < 6; i++) {
        pthread_join(farmers[i], NULL);
    }

    // Түгжээнүүдийг устгаж байна
    pthread_mutex_destroy(&bridge_mutex);

    return 0;
}

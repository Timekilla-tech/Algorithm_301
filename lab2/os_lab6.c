
/* В. Семафор юмуу эсвэл мутекс түгжээг ашиглан уралдааны нөхцлийг заларуул. Decrease_count() функцыг өөрчлөх боломжтой бөгөөд ингэснээр хангалттай нөөцтэй болтлоо процесс дуудах үйлдийг хаах боломжтой болох юм.
Уралдааны нөхцөлийг үгүй хийхийн тулд дундаа ашиглаж байгаа нөөц буюу available_resource хувьсагчид синхрончлогдсон хандалт хийх бүтэцийг бий болгох хэрэгтэй. Үүний тулд мутекс түгжээг ашиглаж болно
*/
#include <pthread.h> 

#define  MAX_RESOURCES 5;
int available_resources = MAX_RESOURCES;
pthread_mutex_t resource_lock = PTHREAD_MUTEX_INITIALIZER;
int decrease_count(int count) {
    pthread_mutex_lock(&resource_lock); // Мутекс түгжээг түгжих ба ингэснээр цор ганц процесс л түүнд хандах боломжыг олгоно
    
    // Хангалттай нөөц байгаа эсэхийг шалгаж байна
    while (available_resources < count) {
        pthread_mutex_unlock(&resource_lock);  // Урсгалыг унтуулахаас өмнө түгжээг нээх хэрэгтэй
        // процесс блоклогсон бөгөөд дохиог(signal) хүлээж байгаа.
        pthread_mutex_lock(&resource_lock);  // Сэрсэний дараагаар дахин түгжинэ.
    }

    // Хэрэв хангалттай нөөц байвал нөөцийг хорогдуулна.
    available_resources -= count;
    
    pthread_mutex_unlock(&resource_lock);  // Мутекс түгжээг тайлна
    return 0;  // Нөөцийг амжилттайгаар олж авлаа
}

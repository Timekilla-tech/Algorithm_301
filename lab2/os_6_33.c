#define MAX_RESOURCES 5
int available_resources = MAX_RESOURCES;
/* decrease available resources by count resources */
/* return 0 if sufficient resources available, */
/* otherwise return -1 */
int decrease_count(int count) {
    if (available_resources < count)
        return -1;
    else {
        available_resources -= count;
        return 0;
    }
}
/* increase available resources by count */
int increase_count(int count) {
    available_resources += count;
    return 0;
}                                              

/* А. Уралдааны нөхцлийг үүсгэж буй өгөгдлийг илэрүүл.
available_resources-хувьсагчид олон төрлийн процесс нэгэн зэрэг хандах боломжтой учраас энэ хувьсагч уралдааны нөхцөл бүрдүүлж байна.

Б. Уралдааны нөхцлийг үүсгэж буй байршлуудыг заа.
Жишээн нь decrease_count(), increase_count() функцууд дээр энэ хувьсагч руу 
зэрэг хандах боломжийг бүрдүүлж байна
*/
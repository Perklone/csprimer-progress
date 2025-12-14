#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool ispangram(char *s) {
    // TODO implement
    uint32_t bs = 0;
    char c;
    while(*s != '\n') {
        c = *s++; // basically it moves it in case we continue;
        if(c <= 65 || c >= 123) continue;
        if ((c >= 65) && (c <= 90)) c += 32;
        bs |= 1 << (c - 97);
    }
    return 0x03ffffff == bs;
}

int main() {
    size_t len;
    ssize_t read;

    char *line = NULL;
    while ((read = getline(&line, &len, stdin)) != -1) {
        if (ispangram(line)) {
            printf("%s", line);
        }
    }

    if (ferror(stdin)) {
        fprintf(stderr, "Error reading from stdin");
    }

    free(line);
    fprintf(stderr, "ok\n");
}
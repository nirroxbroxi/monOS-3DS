#include <stdint.h>

// Adresse du Framebuffer de l'écran supérieur en VRAM
#define VRAM_TOP_LEFT ((volatile uint8_t*)0x18000000)

void main(void) {
    // Remplit l'écran en couleur (Blanc)
    for(int i = 0; i < 400 * 240 * 3; i++) {
        VRAM_TOP_LEFT[i] = 0xFF;
    }

    // Boucle infinie pour maintenir l'OS actif
    while(1);
}

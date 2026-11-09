ifeq ($(strip $(DEVKITARM)),)
$(error "Veuillez définir DEVKITARM dans votre environnement")
endif

include $(DEVKITARM)/base_rules

PREFIX	:=	arm-none-eabi-
CC	:=	$(PREFIX)gcc
OBJCOPY	:=	$(PREFIX)objcopy

CFLAGS	:=	-mthumb -mcpu=arm946e-s -O2 -Wall
LDFLAGS	:=	-specs=nosys.specs -nostartfiles

all: boot.firm

boot.elf: src/main.c
	$(CC) $(CFLAGS) $(LDFLAGS) $< -o $@

boot.bin: boot.elf
	$(OBJCOPY) -O binary $< $@

boot.firm: boot.bin
	python3 generate_firm.py $< $@

clean:
	rm -f boot.elf boot.bin boot.firm

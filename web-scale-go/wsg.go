package main

import (
	"fmt"
	"log"
	S1 "github.com/tarm/serial"
	S2 "github.com/jacobsa/go-serial/serial"

)

func main() {


        c := &S1.Config{Name: "COM45", Baud: 115200}
        s, err := S1.OpenPort(c)
        if err != nil {
                log.Fatal(err)
        }

        n, err := s.Write([]byte("test"))
        if err != nil {
                log.Fatal(err)
        }

        buf := make([]byte, 128)
        n, err = s.Read(buf)
        if err != nil {
                log.Fatal(err)
        }
        log.Printf("%q", buf[:n])
}


func listSerialPorts() {

	options := S2.OpenOptions{
		PortName: "/dev/tty.usbserial-A8008HlV",
		BaudRate: 19200,
		DataBits: 8,
		StopBits: 1,
		MinimumReadSize: 1,
	}

	// Open the port.
	port, err := S2.Open(options)
	if err != nil {
		log.Fatalf("serial.Open: %v", err)
	}

	// Make sure to close it later.
	defer port.Close()

	// Write 4 bytes to the port.
	b := []byte{0x00, 0x01, 0x02, 0x03}
	n, err := port.Write(b)
	if err != nil {
		log.Fatalf("port.Write: %v", err)
	}

	fmt.Println("Wrote", n, "bytes.")

}

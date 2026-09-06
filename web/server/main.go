package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	host := os.Getenv("HOST")
	if host == "" {
		host = "localhost"
	}
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		// fmt.Fprintf(w, `{"message": "Backend server running"}`)
		fmt.Fprintf(w, `{"message": "%s"}`, "Backend server running")
	})

	addr := fmt.Sprintf("%s:%s", host, port)
	fmt.Printf("Backend server running at http://%s/\n", addr)
	err := http.ListenAndServe(addr, nil)

	if err != nil {
		fmt.Println("Error starting server:", err)
	}
}

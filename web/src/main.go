package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
	"net/url"
	"os"
	"path/filepath"
)

func main() {
	host := os.Getenv("HOST")
	if host == "" {
		host = "localhost"
	}
	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}

	// Get the directory where server.go is located
	exePath, err := os.Getwd()
	if err != nil {
		fmt.Println("Error getting working directory:", err)
		return
	}

	// Static file handler - "/" 패턴이 모든 요청을 받음
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Root path로 들어온 요청은 index.html 제공
		if r.URL.Path == "/" {
			indexPath := filepath.Join(exePath, "index.html")
			http.ServeFile(w, r, indexPath)
			return
		}

		// 다른 요청들도 static files에서 서치
		staticPath := filepath.Join(exePath, r.URL.Path)
		http.ServeFile(w, r, staticPath)
	})

	// Proxy to backend server
	backendURL, err := url.Parse("http://localhost:8080")
	if err != nil {
		fmt.Println("Error parsing backend URL:", err)
		return
	}

	http.HandleFunc("/api/", func(w http.ResponseWriter, r *http.Request) {
		proxy := httputil.NewSingleHostReverseProxy(backendURL)
		proxy.ServeHTTP(w, r)
	})

	addr := fmt.Sprintf("%s:%s", host, port)
	fmt.Printf("Front server running at http://%s/\n", addr)
	err = http.ListenAndServe(addr, nil)

	if err != nil {
		fmt.Println("Error starting server:", err)
	}
}

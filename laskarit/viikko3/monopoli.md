monopoli luokkakaavio
```mermaid
classDiagram
        Nappula ..> Ruutu
        Nappula ..> Noppa
        Nappula -- Pelaaja
        Pelaaja .. Ruutu

        
        class Nappula{
            id
            pelaaja id
            ruutu id
            noppa silmäluku
        }
        class Ruutu{
            id
            ruudun nimi
            ruudun omistaja
            seuraava ruutu
        }
        class Noppa{
            noppa silmäluku
        }
        class Pelaaja{
            id
            pelaaja nimi
            pelaaja raha
            pelaaja tontit
            pelaajan nappula    
        }
```


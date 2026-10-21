
import java.util.Random;
import java.util.Scanner;

public class JuegoAdivinaNumero extends Juego {
    protected int numeroAAdivinar;
    protected static final Scanner teclado = new Scanner(System.in);
    protected Random aleatorio = new Random();

    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }

    protected void generaNumero() {
        numeroAAdivinar = aleatorio.nextInt(11);
    }

    public void juega() {
        reiniciaPartida();
        generaNumero();

        while (numeroDeVidas > 0) {
            System.out.print("Adivina un numero entre 0 y 10: ");
            int numero = teclado.nextInt();

            if (!validaNumero(numero)) {
                System.out.println("Numero no valido.");
                continue;
            }

            if (numero == numeroAAdivinar) {
                System.out.println("Acertaste!!");
                actualizaRecord();
                return;
            }

            if (!quitaVida()) {
                System.out.println("Perdiste. El numero era: " + numeroAAdivinar);
                return;
            }

            if (numeroAAdivinar > numero) {
                System.out.println("El numero a adivinar es mayor.");
            } else {
                System.out.println("El numero a adivinar es menor.");
            }
        }
    }
}

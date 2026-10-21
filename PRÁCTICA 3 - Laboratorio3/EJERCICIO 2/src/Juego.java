public class Juego {
    protected int numeroDeVidas;
    protected int record;
    private final int vidasIniciales;

    public Juego(int numeroDeVidas) {
        this.vidasIniciales = numeroDeVidas;
        this.numeroDeVidas = numeroDeVidas;
        this.record = 0;
    }

    public void reiniciaPartida() {
        this.numeroDeVidas = this.vidasIniciales;
    }

    public void actualizaRecord() {
        if (this.numeroDeVidas > this.record) {
            this.record = this.numeroDeVidas;
            System.out.println("Nuevo record: " + this.record);
        }
    }

    public boolean quitaVida() {
        this.numeroDeVidas--;
        return this.numeroDeVidas > 0;
    }
}
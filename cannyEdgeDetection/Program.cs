using System;
using Emgu.CV; // Biblioteca principal de Emgu CV
using Emgu.CV.Structure; // Permite usar tipos como Bgr (color) y Gray (escala de grises)

namespace CannyEdgeDetection
{
    class Program
    {
        static void Main()
        {
            try
            {
                var image = new Image<Bgr, byte>("image3.jpg"); // Cargar la imagen (debe estar en la misma carpeta que el ejecutable)

                var gray = image.Convert<Gray, byte>();// Convertir a escala de grises

                var cannyEdges = gray.Canny(100, 200);// Aplicar detección de bordes con Canny

                CvInvoke.Imshow("Bordes detectados (Canny)", cannyEdges);
                CvInvoke.WaitKey(0); 
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message); // Captura errores
            }
        }
    }
}

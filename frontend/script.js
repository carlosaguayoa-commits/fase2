document.getElementById('transaccion-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const payload = {
        monto: parseFloat(document.getElementById('monto').value),
        hora: parseInt(document.getElementById('hora').value),
        pais_riesgoso: parseInt(document.getElementById('pais_riesgoso').value)
    };

    const box = document.getElementById('resultado-box');

    try {
        const respuesta = await fetch('http://localhost:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!respuesta.ok) {
            throw new Error(`Error en el servidor: ${respuesta.status}`);
        }

        const data = await respuesta.json();

        box.classList.remove('oculto');
        const tagDictamen = document.getElementById('tag-dictamen');
        tagDictamen.innerText = data.resultado;
        tagDictamen.className = data.resultado === 'Fraude' ? 'alerta-fraude' : 'alerta-legitima';

        document.getElementById('prob-fraude').innerText = `${(data.probabilidad_fraude * 100).toFixed(2)}%`;
        document.getElementById('prob-legitima').innerText = `${(data.probabilidad_legitima * 100).toFixed(2)}%`;

    } catch (error) {
        alert("Error al conectar con la API: " + error.message);
    }
});

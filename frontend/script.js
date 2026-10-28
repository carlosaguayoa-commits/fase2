document.getElementById('transaccion-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const monto = document.getElementById('monto').value;
    const hora = document.getElementById('hora').value;
    const pais_riesgoso = document.getElementById('pais_riesgoso').value;
    const box = document.getElementById('resultado-box');

    const payload = {
        monto: parseFloat(monto),
        hora: parseInt(hora),
        pais_riesgoso: parseInt(pais_riesgoso)
    };

    try {
        const respuesta = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!respuesta.ok) {
            throw new Error(`Error en servidor: ${respuesta.status}`);
        }

        const data = await respuesta.json();

        box.classList.remove('oculto');
        const tagDictamen = document.getElementById('tag-dictamen');
        tagDictamen.innerText = data.resultado;
        tagDictamen.className = data.resultado === 'Fraude' ? 'alerta-fraude' : 'alerta-legitima';

        document.getElementById('prob-fraude').innerText = `${(data.probabilidad_fraude * 100).toFixed(2)}%`;
        document.getElementById('prob-legitima').innerText = `${(data.probabilidad_legitima * 100).toFixed(2)}%`;

    } catch (error) {
        alert("No se pudo conectar con la API: " + error.message);
    }
});

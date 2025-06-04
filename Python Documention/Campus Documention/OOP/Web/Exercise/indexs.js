function sapa() {
    alert('Berhasil Klik');
}

function penjumlahan() {
    var x = 16;
    var y = 6;
    return x + y;
}

function input() {
    s = document.forms[0].q.value;
    q = document.forms[0].pesan.value;
    alert('Kamu mencari mengenai : ', s);
}

function input_hasil() {
    p = document.hitung.panjang.value;
    l = document.hitung.lebar.value;
    luas = parseInt(p*l);
    document.hitung.hsl.value = luas;
    document.getElementById('hasil').innerHTML='Luas = '+luas;
}
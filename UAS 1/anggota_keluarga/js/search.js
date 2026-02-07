/**
 * Fungsi untuk menampilkan daftar anggota keluarga ke dalam grid.
 * @param {string} filterText - Kata kunci pencarian nama.
 */
function tampilkanKeluarga(filterText = "") {
    const listContainer = document.getElementById('memberList');
    const resultCountBadge = document.getElementById('searchResultCount');
    
    if (!listContainer) return;
    
    const dataFiltered = dataKeluarga.filter(item => {
        const nama = item.Nama_Lengkap ? item.Nama_Lengkap.toLowerCase() : "";
        return nama.includes(filterText.toLowerCase());
    });
    
    if (resultCountBadge) {
        if (filterText === "") {
            resultCountBadge.innerText = `Menampilkan ${dataFiltered.length} total anggota keluarga`;
        } else {
            resultCountBadge.innerText = `Ditemukan ${dataFiltered.length} anggota untuk "${filterText}"`;
        }
    }
    
    listContainer.innerHTML = "";
    
    const limitData = filterText === "" ? dataFiltered.slice(0, 20) : dataFiltered;
    
    limitData.forEach(person => {
        const isMale = person.Jenis_Kelamin === 'Laki-laki';
        const genderClass = isMale ? 'male' : 'female';
        
        let infoPasanganHtml = "";
        if (person.Status_Nikah === "Menikah") {
            const pasangan = dataKeluarga.find(p => p.ID === person.ID_Pasangan);
            
            let namaPasangan = "";
            if (pasangan) {
                namaPasangan = pasangan.Nama_Lengkap;
            } else if (person.Nama_Pasangan) {
                namaPasangan = person.Nama_Pasangan;
            } else {
                namaPasangan = "Tidak terdata";
            }

            const labelPasangan = isMale ? "Istri" : "Suami";
            const iconPasangan = isMale ? "👩" : "👨";
            infoPasanganHtml = `
                <div class="spouse-box" style="background: #fdf2f8; padding: 10px; border-radius: 8px; margin-top: 10px; border-left: 4px solid #ec4899;">
                    <small style="color: #be185d; font-weight: bold; display: block; margin-bottom: 2px;">${iconPasangan} ${labelPasangan.toUpperCase()}:</small>
                    <span style="color: #334155; font-weight: 500;">${namaPasangan}</span>
                </div>
            `;
        }

        const card = document.createElement('div');
        card.className = `card ${genderClass}`;
        
        card.innerHTML = `
            <div class="card-content" style="position: relative; padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 15px;">
                <span class="status-badge" style="background: #e2e8f0; padding: 4px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: 600;">${person.Peran}</span>
                <h3 style="margin: 10px 0 5px 0; color: #1e293b;">${person.Nama_Lengkap}</h3>
                <div class="card-info" style="font-size: 0.85rem; color: #64748b;">
                    <p>🆔 ID Member: #${person.ID}</p>
                    <p>👫 Status: ${person.Status_Nikah}</p>
                    ${infoPasanganHtml}
                </div>
                <button class="btn-detail" 
                        onclick="window.location.href='detail.html?id=${person.ID}'" 
                        style="width: 100%; margin-top: 15px; padding: 10px; background: #2563eb; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600;">
                    Buka Profil Silsilah
                </button>
            </div>
        `;
        listContainer.appendChild(card);
    });

    if (dataFiltered.length === 0) {
        listContainer.innerHTML = `<div class="no-result" style="grid-column: 1/-1; text-align: center; padding: 40px; color: #94a3b8;">Silsilah tidak ditemukan.</div>`;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    tampilkanKeluarga();
    const input = document.getElementById('searchInput');
    if (input) {
        input.addEventListener('input', (e) => tampilkanKeluarga(e.target.value));
    }
});
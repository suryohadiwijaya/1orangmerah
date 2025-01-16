class SoccerTeam:
    def __init__(self, formation):
        # Inisialisasi dengan formasi awal
        self.formation = formation
        self.players = self.generate_players(formation)
    
    def generate_players(self, formation):
        # Generate daftar pemain berdasarkan formasi
        players = []
        positions = ["GK"] + ["DF"] * formation[0] + ["MF"] * formation[1] + ["FW"] * formation[2]
        for i, position in enumerate(positions):
            players.append(f"{position}{i+1}")
        return players

    def remove_player(self, player_id):
        # Hapus pemain yang mendapatkan kartu merah
        if player_id in self.players:
            self.players.remove(player_id)
        else:
            print(f"Player {player_id} not found in the team.")
    
    def display_formation(self):
        # Tampilkan formasi saat ini
        print("Current formation:")
        print(f"Goalkeeper: {self.players[0]}")
        print(f"Defenders: {', '.join([p for p in self.players if 'DF' in p])}")
        print(f"Midfielders: {', '.join([p for p in self.players if 'MF' in p])}")
        print(f"Forwards: {', '.join([p for p in self.players if 'FW' in p])}")

# Contoh penggunaan
initial_formation = (4, 4, 2)  # 4 Bek, 4 Gelandang, 2 Penyerang
team = SoccerTeam(initial_formation)
team.display_formation()

# Misalkan pemain MF2 mendapatkan kartu merah
team.remove_player("MF2")
print("\nAfter red card:")
team.display_formation()

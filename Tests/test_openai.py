import openai

# Replace YOUR_API_KEY with your actual OpenAI API key
openai.api_key = "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"

def chat_with_gpt():
        # Use OpenAI API to get the response
    try:
        response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": "(n'ecris pas d'autres reponse que le dictionnaire)a partir de un ticket de caisse, cree un dictionnaire python avec les infos importantes (inclue dans le dictionnaire, 'Nom du magasin', 'Adresse', 'Date',   'Total', 'Type de paiement', 'Articles', dans 'Articles' fais un sous dictionnaire avec 'Nom_article', 'Catégorie' (choisi les toi-même), 'Prix') voici le ticket de caisse Naegel MAISON NAEGEL 9 RUE DES ORFEVRES 67000 STRASBOURG France Siret 71850045700012 APE 1071DTVA FR72718500457 Tel 03 68 32 62 86 5456 90 EUR Ticket (VTE) 1-824641.1 12210 Edité le 24/09/2024 à 15:19:15 1 client SARO (9) Ote Designation PU.€ Net.€ 1 LUNETTE AU FLAN 1.90 1.90 1 THE BROT 1.20 1.20 B 2 PP A L'HUILE D'OLIVE 1.20 2.40  1 PAIN CIABATTA 3.70 3.70 A 1 SACHET 0.10 0.10 C mb Catégories à identi Total 9.30€ Hors Taxes Reçu ESPECES (1x9.30€) 5/6 9.00€ 9.30€ HT 0.08€ TTC 0.10€ TVA TVA (C) & 20.00% 0.02€ TVA (8) a 5.50%  5.21€ 5.50€ 0.296 TVA (A) & 0.00%3.70€3.70€ 0.00€"}]
            )

            # Extract the response from OpenAI
        chat_response = response['choices'][0]['message']['content']
        ticket_dic = chat_response

            # Add the assistant's response to the conversation
        print(ticket_dic)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_gpt()

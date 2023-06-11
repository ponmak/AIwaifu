from chat_downloader import ChatDownloader

url = " "
chat = ChatDownloader().get_chat(url)
for message in chat:
    chat.print_formatted(message)
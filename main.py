from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/957640927592202351/1Xo0BM52Njqh7MUk14wpN8eKE729mRMLf7PORj-cvF5u6G-XlQ3ttSXbfiP8w0pfLeSJ", username="TestUser")

embed = DiscordEmbed(
    title="Lvl ?? | chat channel 12 ", description="Ut enim ad minima veniam, nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus! Ut enim ad minim veniam, nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, sunt in culpa qui officia deserunt mollit anim id est laborum", color='03b2f8'
)
webhook.add_embed(embed)
response = webhook.execute()
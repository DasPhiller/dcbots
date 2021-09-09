const { Client, Intents, ClientUser} = require('discord.js');

const client = new Client({
    intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.GUILD_MEMBERS]
});

client.on('ready', () => {
    console.log('Bot Gestartet')

    const commands = [
        {
            name: 'piep',
            description: 'Sagt piep',
            options: null
        },
        {
            name: 'blub',
            description: 'sagt blub',
            options: null
        },
        {
            name: 'test',
            description: 'test',
            options: null
        }
    ]

    // client.application?.commands.set(data);

    client.guilds.cache.get('841224672137576458').commands.set(commands);
});
client.on('interactionCreate', interaction => {
    if (interaction.isCommand()) {
        if (interaction.commandName == 'piep') {
            interaction.reply('<@' + interaction.user.id + '>');
        }
        if (interaction.commandName == 'blub') {
            interaction.reply('Blub Blub weg war er/sie')
        }
        if (interaction.commandName == 'test') {
            interaction.reply('Dies ist ein Test <@' + interaction.user.id + ">")
        }
    }
})
/*
client.on('messageCreate', message => {
    if (message.author.bot) return;
    console.log(message.content);
    console.log(message.author.id)
    message.channel.send('hiv2')
})
*/

client.login("ODgxNDY2NTkzNjQ3OTIzMjIx.YStPvA.JT3OKMs31bPgDrfQ27GKN8Fg13w")